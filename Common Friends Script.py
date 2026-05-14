import pandas as pd
karl_id = users[users['user_name'] == 'Karl']['user_id'].iloc[0]
hans_id = users[users['user_name'] == 'Hans']['user_id'].iloc[0]
karl_friends = friends[friends['user_id'] == karl_id]['friend_id']
hans_friends = friends[friends['user_id'] == hans_id]['friend_id']
mutual_friend_ids = karl_friends[karl_friends.isin(hans_friends)]
result = users[users['user_id'].isin(mutual_friend_ids)][['user_id', 'user_name']]
print(result)
