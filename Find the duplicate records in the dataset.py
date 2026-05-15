import pandas as pd
duplicates = title.groupby(['worker_title', 'affected_from']).size().reset_index(name='count')
duplicate_records = duplicates[duplicates['count'] > 1]
print(duplicate_records)
