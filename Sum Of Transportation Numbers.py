import pandas as pd
min_val = transportation_numbers['number'].min()
max_val = transportation_numbers['number'].max()
total_sum = transportation_numbers['number'].sum()
summation = total_sum - min_val - max_val
result = pd.DataFrame({
    'min_number': [min_val],
    'max_number': [max_val],
    'summation': [summation]
})

print(result)
