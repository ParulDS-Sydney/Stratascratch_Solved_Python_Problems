import pandas as pd
merged_df=pd.merge(google_competition_participants,google_competition_scores,on='member_id')
team_avg=merged_df.groupby('team_id')['member_score'].mean().reset_index()
result=team_avg.sort_values(by='member_score',ascending=False)
print(result)
