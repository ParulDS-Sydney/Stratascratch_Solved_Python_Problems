import pandas as pd
logins_2016 = product_logins[product_logins['login_date'].dt.year == 2016]
result = logins_2016['account_id'].nunique()
print(result)
