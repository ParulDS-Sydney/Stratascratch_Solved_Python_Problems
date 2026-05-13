import pandas as pd
result=google_file_store[(google_file_store['filename'].str.contains('draft',case=False,na=False))&(google_file_store['contents'].str.contains('optimism', case=False, na=False))
]
print(result)
