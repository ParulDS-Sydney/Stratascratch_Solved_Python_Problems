import pandas as pd
sold_product_ids = sales_transactions['product_id'].unique()
unsold_products = inventory_current_stock[~inventory_current_stock['product_id'].isin(sold_product_ids)]
result = unsold_products[['product_id', 'product_name']]

print(result)
