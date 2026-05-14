import pandas as pd
merged_df = pd.merge(playbook_events, playbook_users, on='user_id')
filtered_df = merged_df[
    (merged_df['device'] == 'macbook pro') & 
    (merged_df['location'] == 'Argentina') & 
    (merged_df['language'] != 'spanish')
]
result = filtered_df.groupby(['company_id', 'language']).size().reset_index(name='event_count')
print(result)
