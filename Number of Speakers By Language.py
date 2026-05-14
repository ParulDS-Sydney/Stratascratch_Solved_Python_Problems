import pandas as pd
merged_df = pd.merge(playbook_events, playbook_users, on='user_id')
result = merged_df.groupby(['location', 'language'])['user_id'].nunique().reset_index()
result.columns = ['country', 'language', 'n_speakers']
result = result.sort_values(by='country')
print(result)
