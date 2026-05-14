import pandas as pd
merged_df = pd.merge(user_flags, flag_review, on='flag_id')
grouped = merged_df.groupby(['user_firstname', 'user_lastname'])
result = grouped.agg(
    n_distinct_videos_reviewed=('video_id', 'nunique'),
    latest_review_date=('reviewed_date', 'max')
).reset_index()
removed_videos = merged_df[merged_df['reviewed_outcome'] == 'removed']
removed_counts = removed_videos.groupby(['user_firstname', 'user_lastname'])['video_id'].nunique().reset_index()
removed_counts.columns = ['user_firstname', 'user_lastname', 'n_distinct_videos_removed']
final_result = pd.merge(result, removed_counts, on=['user_firstname', 'user_lastname'], how='left')
final_result['n_distinct_videos_removed'] = final_result['n_distinct_videos_removed'].fillna(0)
print(final_result)
