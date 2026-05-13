import pandas as pd
min_id=worker['worker_id'].min()
result=worker[worker['worker_id']==min_id]
print(result)
