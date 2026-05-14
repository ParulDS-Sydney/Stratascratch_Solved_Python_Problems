import pandas as pd
merged_df = pd.merge(orders, customers, left_on='cust_id', right_on='id', how='left')
shippable_count = merged_df['address'].notnull().sum()
total_orders = len(orders)
percentage_shippable = (shippable_count / total_orders) * 100
print(f"Percentage of shippable orders: {percentage_shippable}%")
