import pandas as pd
import numpy as np
from functools import reduce
from rename import rename

benchmark_list = [
    "lmarena_text",
    "terminalbenchhard",
    "aalcr",
    "omniscience",
    "hle",
    "gpqadiamond",
    "scicode",
    "ifbench",
    "critpt",
    "mmmupro",
    "gdpvalaa",
]

"""
The weighting of all benchmarks in Artificial Analysis strictly adheres to
Artificial Analysis' official v4 standard
"""
index_weights = {
    "lmarena_text": 0.30,
    "gdpvalaa": 0.1169,
    "mmmupro": 0.0581,
    "terminalbenchhard": 0.1169,
    "scicode": 0.0581,
    "aalcr": 0.04375,
    "omniscience": 0.0875,
    "ifbench": 0.04375,
    "hle": 0.0875,
    "gpqadiamond": 0.04375,
    "critpt": 0.04375,
}
board_weights = index_weights

def weighted_sum_percent(dataframe: pd.DataFrame, board_weights: dict) -> pd.DataFrame:
    weight_series = pd.Series(board_weights, index=dataframe.columns).astype(float).fillna(0.0)
    scores = dataframe.astype(float).copy()
    max_scores = scores.max(axis=0, skipna=True)
    percent = scores.div(max_scores, axis=1).mul(100.0).fillna(0.0)
    weighted_score = percent.mul(weight_series, axis=1).sum(axis=1)
    results = pd.DataFrame({"weighted_score": weighted_score})
    results["ranking"] = results["weighted_score"].rank(ascending=False, method="min").astype(int)
    return results.sort_values("ranking")


data = {}
for name in benchmark_list:
    df = pd.read_csv(f"leaderboards/{name}.csv", usecols=["Name", "Score"])
    df["Score"] = pd.to_numeric(df["Score"], errors="coerce")
    df["canonical"] = df["Name"].apply(rename)
    df = df.sort_values("Score", ascending=False).drop_duplicates("canonical")
    df = df.rename(columns={"Name": f"{name} Name", "Score": name})
    data[name] = df

df = reduce(lambda l, r: pd.merge(l, r, on="canonical", how="outer"), data.values())

score_columns = benchmark_list
df_scores = df[["canonical"] + score_columns].copy()

ensemble_df = weighted_sum_percent(df_scores.set_index("canonical")[score_columns], board_weights)
df_out = pd.concat([df_scores.set_index("canonical"), ensemble_df], axis=1).reset_index()
df_out = df_out.sort_values("ranking")
df_out.to_excel("LLM_leaderboard.xlsx", index=False)

