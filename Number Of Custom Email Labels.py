import pandas as pd
merged_df = pd.merge(google_gmail_emails, google_gmail_labels, left_on='id', right_on='email_id')
result = merged_df.groupby(['to_user', 'label']).size()
print(result)
