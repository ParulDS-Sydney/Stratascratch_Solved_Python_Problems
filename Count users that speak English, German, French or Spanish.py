import pandas as pd
target_languages = ['english', 'german', 'french', 'spanish']
filtered_users = playbook_users[playbook_users['language'].isin(target_languages)]
result = filtered_users['user_id'].nunique()
print(result)
