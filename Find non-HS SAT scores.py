import pandas as pd
result = sat_scores[~sat_scores['school'].str.endswith('HS', na=False)]
print(result)
