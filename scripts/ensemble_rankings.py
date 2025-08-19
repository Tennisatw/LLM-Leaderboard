import pandas as pd
import numpy as np
from typing import Optional, Tuple, Dict
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import TruncatedSVD

def _to_dataframe(data) -> pd.DataFrame:
    if isinstance(data, pd.DataFrame):
        return data.copy()
    raise ValueError("Input must be a pandas.DataFrame where rows are models and columns are leaderboards.")

def _standardize_per_board(df: pd.DataFrame) -> Tuple[pd.DataFrame, Dict[str, Tuple[float, float]]]:
    """
    Z-score standardize each leaderboard (column) using observed values only.
    Returns standardized DataFrame and dict of (mean, std) per column.
    """
    stats = {}
    df_std = df.copy().astype(float)
    for col in df.columns:
        col_vals = df[col].astype(float)
        mu = col_vals.mean(skipna=True)
        sigma = col_vals.std(skipna=True, ddof=0)
        # guard against zero std
        if pd.isna(sigma) or sigma == 0:
            # leave as zeros after centering
            sigma = 1.0
        stats[col] = (mu, sigma)
        df_std[col] = (col_vals - mu) / sigma
    return df_std, stats

def aggregate_zscore_mean(df: pd.DataFrame, min_obs: int = 2) -> pd.Series:
    """
    1) Z-score each column, 2) take row-wise mean over available columns.
    Returns a score series (higher is better).
    """
    df = _to_dataframe(df)
    df_std, _ = _standardize_per_board(df)
    counts = df_std.notna().sum(axis=1)
    # mean over available columns
    score = df_std.mean(axis=1, skipna=True)
    score[counts < min_obs] = np.nan
    return score.rename("z_mean_score")

def aggregate_borda(df: pd.DataFrame, higher_is_better: bool = True, min_obs: int = 2) -> pd.Series:
    """
    Rank aggregation via Borda count. For each column:
      - compute ranks (descending if higher_is_better)
      - convert to [0,1] by (max_rank - rank) / (max_rank - 1) for that column's observed rows
    Then average across columns.
    Returns a score series in [0,1] (higher is better).
    """
    df = _to_dataframe(df)
    # Prepare a score DataFrame to hold per-board normalized Borda scores
    borda = pd.DataFrame(index=df.index, columns=df.columns, dtype=float)
    for col in df.columns:
        col_vals = df[col].dropna()
        if col_vals.empty:
            continue
        # rank: 1 is best if higher_is_better else lowest score best
        ascending = not higher_is_better
        ranks = col_vals.rank(ascending=ascending, method="average")
        max_rank = ranks.max()
        if max_rank == 1:  # only one observed -> give full credit 1.0
            norm = pd.Series(1.0, index=ranks.index)
        else:
            # Convert to [0,1]: best gets 1.0, worst gets 0.0
            norm = (max_rank - ranks) / (max_rank - 1)
        borda.loc[norm.index, col] = norm
    counts = borda.notna().sum(axis=1)
    score = borda.mean(axis=1, skipna=True)
    score[counts < min_obs] = np.nan
    return score.rename("borda_score")

def _svd_impute(df_std: pd.DataFrame, rank: int = 3, n_iter: int = 25, random_state: int = 0) -> pd.DataFrame:
    """
    Masked low-rank reconstruction on the standardized matrix.
    Steps:
      1) Initialize missing with column means (which are ~0 after standardization).
      2) Iterate:
          - Fit TruncatedSVD on the filled matrix (no centering needed because standardized already).
          - Reconstruct low-rank approximation.
          - Put back observed entries (do not let them drift).
    Returns a fully-filled DataFrame.
    """
    X = df_std.to_numpy(dtype=float)
    mask = ~np.isnan(X)
    # init: column means (nanmean) -> for standardized matrix means ≈ 0
    col_means = np.nanmean(X, axis=0)
    X_filled = np.where(mask, X, np.take(col_means, np.arange(X.shape[1])))

    svd = TruncatedSVD(n_components=min(rank, min(X.shape)-1), random_state=random_state)
    for _ in range(n_iter):
        # Fit SVD on current fill
        Z = svd.fit_transform(X_filled)    # shape (n_samples, rank)
        W = svd.components_               # shape (rank, n_features)
        X_hat = Z @ W                     # low-rank reconstruction
        # Keep observed entries fixed
        X_filled = np.where(mask, X, X_hat)
    return pd.DataFrame(X_filled, index=df_std.index, columns=df_std.columns)

def aggregate_svd_impute(df: pd.DataFrame, rank: int = 3, min_obs: int = 1) -> pd.Series:
    """
    Pipeline:
      - Z-score per board
      - SVD impute missing values on standardized matrix
      - Row-wise mean of the imputed standardized scores
    Returns a score series (higher is better).
    """
    df = _to_dataframe(df)
    df_std, _ = _standardize_per_board(df)
    X_imp = _svd_impute(df_std, rank=rank)
    # even if a row had zero obs, imputation provides values; optional: require min_obs
    counts = df.notna().sum(axis=1)
    score = X_imp.mean(axis=1)
    score[counts < min_obs] = np.nan
    return score.rename("svd_impute_score")

def compute_ensemble_rankings(
    df: pd.DataFrame,
    higher_is_better: bool = True,
    min_obs_mean: int = 2,
    min_obs_borda: int = 2,
    svd_rank: int = 3,
    min_obs_svd: int = 1,
    consensus: str = "avg_rank",  # options: "avg_rank" or "avg_z"
) -> pd.DataFrame:
    """
    Given a DataFrame (rows=models, cols=leaderboards), compute:
      - z_mean_score
      - borda_score
      - svd_impute_score
    Then produce ranks (1=best) for each, and a consensus rank.
    """
    # Compute scores
    # z_mean = aggregate_zscore_mean(df, min_obs=min_obs_mean)
    # borda = aggregate_borda(df, higher_is_better=higher_is_better, min_obs=min_obs_borda)
    svd_s = aggregate_svd_impute(df, rank=svd_rank, min_obs=min_obs_svd)

    out = pd.DataFrame({
        # "z_mean_score": z_mean,
        # "borda_score": borda,
        "total_score": svd_s,
    })

    # Convert scores to ranks (1=best). For NaNs, rank them at the bottom by placing them after max.
    def score_to_rank(series: pd.Series, ascending: bool = False) -> pd.Series:
        # ascending=False because higher score is better
        ranks = series.rank(ascending=ascending, method="min")
        # put NaNs at bottom: set them to max rank + 1
        max_rank = np.nanmax(ranks.to_numpy())
        ranks = ranks.where(series.notna(), max_rank + 1)
        return ranks.astype(int)

    # out["z_mean_rank"] = score_to_rank(out["z_mean_score"], ascending=False)
    # out["borda_rank"] = score_to_rank(out["borda_score"], ascending=False)
    out["ranking"] = score_to_rank(out["total_score"], ascending=False)

    # # Consensus
    # if consensus == "avg_rank":
    #     out["consensus_rank"] = out[["z_mean_rank", "borda_rank", "svd_impute_rank"]].mean(axis=1)
    # elif consensus == "avg_z":
    #     # Standardize the three scores then average; then convert to rank
    #     z3 = out[["z_mean_score", "borda_score", "svd_impute_score"]].apply(
    #         lambda s: (s - s.mean(skipna=True)) / (s.std(skipna=True, ddof=0) if s.std(skipna=True, ddof=0) not in [0, np.nan] else 1.0)
    #     )
    #     combo = z3.mean(axis=1)
    #     # turn into rank
    #     combo_rank = combo.rank(ascending=False, method="min")
    #     max_rank = np.nanmax(combo_rank.to_numpy())
    #     out["consensus_rank"] = combo_rank.where(combo.notna(), max_rank + 1)
    # else:
    #     raise ValueError("consensus must be 'avg_rank' or 'avg_z'")

    # Final sort by consensus_rank, then by svd_impute_rank as tie-breaker
    # out = out.sort_values(by=["consensus_rank", "svd_impute_rank", "z_mean_rank", "borda_rank"])
    return out

def demo_synthetic(n_models: int = 150, n_boards: int = 8, missing_rate: float = 0.5, random_state: int = 0) -> pd.DataFrame:
    """
    Generate a synthetic dataset where each model has a latent skill theta,
    each board has a bias b_j, and observed scores are theta + b_j + noise.
    Then randomly drop entries according to missing_rate.
    """
    rng = np.random.default_rng(random_state)
    theta = rng.normal(0, 1, size=n_models)          # model skill
    bias = rng.normal(0, 1, size=n_boards)           # board difficulty / shift
    noise = rng.normal(0, 0.8, size=(n_models, n_boards))

    X = theta[:, None] + bias[None, :] + noise       # raw scores
    # simulate positive scales per board
    scales = rng.uniform(5, 20, size=n_boards)
    X = X * scales[None, :] + rng.uniform(50, 80, size=n_boards)[None, :]

    # introduce missingness
    mask = rng.random(size=X.shape) < missing_rate
    X[mask] = np.nan

    models = [f"model_{i+1}" for i in range(n_models)]
    boards = [f"board_{j+1}" for j in range(n_boards)]
    df = pd.DataFrame(X, index=models, columns=boards)
    return df