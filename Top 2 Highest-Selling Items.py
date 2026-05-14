import pandas as pd
product_sales = ecommerce_transactions.groupby(['category', 'product_name'])['quantity'].sum().reset_index()
product_sales = product_sales.sort_values(
    by=['category', 'quantity', 'product_name'], 
    ascending=[True, False, True]
)
product_sales['rank'] = product_sales.groupby('category')['quantity'].rank(
    method='first', 
    ascending=False
)
result = product_sales[product_sales['rank'] <= 2]
print(result[['category', 'product_name', 'quantity', 'rank']])
