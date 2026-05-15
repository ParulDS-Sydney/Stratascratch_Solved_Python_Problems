import pandas as pd
spanish_speakers = playbook_users[playbook_users['language'] == 'spanish']
merged_data = pd.merge(spanish_speakers, playbook_events, on='user_id')
logins = merged_data[merged_data['event_name'] == 'login']
result = logins.groupby('location').size().reset_index(name='n_logins')
result = result.sort_values(by='n_logins', ascending=False)
print(result)
