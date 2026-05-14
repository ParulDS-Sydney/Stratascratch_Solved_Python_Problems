import pandas as pd
result = user_sessions.groupby('platform')['user_id'].nunique().reset_index()
result.columns = ['platform', 'n_users']
print(result)
