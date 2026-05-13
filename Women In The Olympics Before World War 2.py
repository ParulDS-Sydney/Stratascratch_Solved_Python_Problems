import pandas as pd
filtered_df=olympics_athletes_events[(olympics_athletes_events['sex']=='F')&(olympics_athletes_events['year']<1939)]
unique_names=filtered_df['name'].unique()
result_df=pd.DataFrame(unique_names,columns=['name'])
print(result_df)
