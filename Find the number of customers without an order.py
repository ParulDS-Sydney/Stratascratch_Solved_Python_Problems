import pandas as pd
merged_df = pd.merge(customers, orders, left_on='id', right_on='cust_id', how='left')
no_order_customers = merged_df[merged_df['id_y'].isnull()]
result = len(no_order_customers)
print(result)
