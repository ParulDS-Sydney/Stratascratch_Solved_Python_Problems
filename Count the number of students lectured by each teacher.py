import pandas as pd
result = sat_scores.groupby('teacher').size()
print(result)
