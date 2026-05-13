import pandas as pd

doctors_johnson = employee_list[
    (employee_list['last_name'] == 'Johnson') & 
    (employee_list['profession'] == 'Doctor')
]
result = doctors_johnson[['first_name', 'last_name']]

print(result)
