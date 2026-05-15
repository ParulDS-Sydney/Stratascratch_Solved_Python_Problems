import pandas as pd
negative_reviews_df = hotel_reviews[hotel_reviews['negative_review'] != 'No Negative']
result = negative_reviews_df.groupby('reviewer_nationality').size().reset_index(name='negative_review_count')
result = result.sort_values(by='negative_review_count', ascending=False)
print(result)
