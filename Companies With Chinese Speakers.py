import pandas as pd
chinese_users=playbook_users[playbook_users['language']=='chinese']
company_counts = chinese_users.groupby('company_id').size().reset_index(name='speaker_count')
result = company_counts[company_counts['speaker_count'] >= 2][['company_id']]
print(result)
