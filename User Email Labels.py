import pandas as pd
merged_df = pd.merge(google_gmail_emails, google_gmail_labels, left_on='id', right_on='email_id')
target_labels = ['Promotion', 'Social', 'Shopping']
filtered_df = merged_df[merged_df['label'].isin(target_labels)]
result = filtered_df.pivot_table(index='to_user', 
                                 columns='label', 
                                 values='id', 
                                 aggfunc='count', 
                                 fill_value=0).reset_index()
result.columns.name = None 

print(result)
