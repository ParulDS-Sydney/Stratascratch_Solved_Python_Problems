import pandas as pd
class_mapping = {1: 'First class', 2: 'Second class', 3: 'Third class'}
titanic['passenger_class'] = titanic['pclass'].map(class_mapping)
report = titanic.groupby(['passenger_class', 'survived']).size().unstack(fill_value=0)
report.columns = ['non_survivors', 'survivors']
report = report.reset_index()
print(report)
