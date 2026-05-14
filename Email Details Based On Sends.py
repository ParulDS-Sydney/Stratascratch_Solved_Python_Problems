import pandas as pd
senders = google_gmail_emails.groupby('day')['from_user'].nunique().reset_index()
senders.columns = ['day', 'sender_count']
receivers = google_gmail_emails.groupby('day')['to_user'].nunique().reset_index()
receivers.columns = ['day', 'receiver_count']
counts_df = pd.merge(senders, receivers, on='day')
valid_days = counts_df[counts_df['receiver_count'] > counts_df['sender_count']]['day']
result = google_gmail_emails[google_gmail_emails['day'].isin(valid_days)]
print(result)

