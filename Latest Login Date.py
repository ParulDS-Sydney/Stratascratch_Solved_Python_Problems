import pandas as pd
result = players_logins.groupby('player_id')['login_date'].max().reset_index()
print(result)
