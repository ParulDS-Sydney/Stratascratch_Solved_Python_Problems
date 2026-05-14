import pandas as pd
result = google_salaries.groupby('education')['salary'].mean().reset_index()
print(result)
