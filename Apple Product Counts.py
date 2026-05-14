import pandas as pd
merged_df = pd.merge(playbook_events, playbook_users, on='user_id')
apple_devices = ['macbook pro', 'iphone 5s', 'ipad air']
total_users = merged_df.groupby('language')['user_id'].nunique().reset_index(name='total_users')
apple_users_df = merged_df[merged_df['device'].isin(apple_devices)]
apple_counts = apple_users_df.groupby('language')['user_id'].nunique().reset_index(name='n_apple_users')
result = pd.merge(total_users, apple_counts, on='language', how='left')
result['n_apple_users'] = result['n_apple_users'].fillna(0)
result = result.sort_values(by='total_users', ascending=False)
print(result[['language', 'n_apple_users', 'total_users']])
