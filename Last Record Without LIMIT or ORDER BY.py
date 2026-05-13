import pandas as pd
max_id = worker['worker_id'].max()
result = worker[worker['worker_id']== max_id]
print(result)
