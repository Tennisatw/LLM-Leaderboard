import pandas as pd
from functools import reduce
from scripts.rename import rename
from scripts.ensemble_rankings import compute_ensemble_rankings

# Read all raw leaderboards
data_list = ['arenatext', 'mmlupro', 'gpqadiamond', 'hle', 'aalcr', 'aime2025', 'lcb', 'mmmu']
data = {}
for name in data_list:
    df = pd.read_csv(f'leaderboards/leaderboard_{name}.csv', usecols=["Name", "Score"])
    df['canonical'] = df['Name'].apply(rename)
    df = df.sort_values('Score', ascending=False).drop_duplicates('canonical')

    df = df.rename(columns={'Name':f'{name} Name', 'Score':f'{name} Score'})
    data[name] = df

data['mmmu']['mmmu Score'] = pd.to_numeric(data['mmmu']['mmmu Score'], errors='coerce')

df = reduce(lambda l,r: pd.merge(l, r, on='canonical', how='outer'), data.values())

cols = list(df.columns)
cols.insert(0, cols.pop(cols.index("canonical")))
df = df[cols]

df.to_excel('leaderboard_raw.xlsx', index=False)

score_columns = [f'{name} Score' for name in data_list]
df = df[['canonical'] + score_columns]

# Keep only models that appear in more than 1 leaderboards
appearance_count = df.notna().sum(axis=1)
df = df[appearance_count > 2]

# Compute ensemble rankings
ensemble_df = compute_ensemble_rankings(
    df[score_columns], 
    higher_is_better=True, 
    svd_rank=3, 
)
# conbine with original df
df = pd.concat([df, ensemble_df], axis=1)
df = df.sort_values('ranking')
df['ranking'] = df['ranking'].round(4)

# df.to_csv('leaderboard.csv', index=False)
df.to_excel('leaderboard.xlsx', index=False)

