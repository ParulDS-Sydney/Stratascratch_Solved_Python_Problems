import pandas as pd
friends = google_friends_network.copy()
reversed_friends = friends.rename(columns={'user_id': 'friend_id', 'friend_id': 'user_id'})
symmetric_network = pd.concat([friends, reversed_friends], ignore_index=True).drop_duplicates()
print(symmetric_network)
