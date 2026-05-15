import pandas as pd
survivors = titanic[titanic['survived'] == 1]
result = survivors.pivot_table(index='sex', 
                               columns='pclass', 
                               values='passengerid', 
                               aggfunc='count', 
                               fill_value=0)
result.columns = ['first_class', 'second_classs', 'third_class']
result = result.reset_index()
print(result)
