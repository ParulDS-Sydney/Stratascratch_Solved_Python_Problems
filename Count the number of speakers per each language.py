import pandas as pd
result = playbook_users.groupby('language').size().reset_index(name='n_speakers')
result = result.sort_values(by='n_speakers', ascending=False)
print(result)
