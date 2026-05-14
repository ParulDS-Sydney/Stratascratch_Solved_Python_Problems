import pandas as pd
email_counts = google_gmail_emails.groupby('from_user').size().reset_index(name='total_emails')
email_counts['rank'] = email_counts['total_emails'].rank(method='first', ascending=False)
result = email_counts.sort_values(by='rank')
print(result)
