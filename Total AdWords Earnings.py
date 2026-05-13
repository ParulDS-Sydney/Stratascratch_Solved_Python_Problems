import pandas as pd
result=google_adwords_earnings.groupby('business_type')['adwords_earnings'].sum().reset_index()
print(result)
