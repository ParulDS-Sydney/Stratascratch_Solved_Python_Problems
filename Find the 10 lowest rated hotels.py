import pandas as pd
unique_hotels = hotel_reviews[['hotel_name', 'average_score']].drop_duplicates()
lowest_10_hotels = unique_hotels.nsmallest(10, 'average_score', keep='all')
result = lowest_10_hotels[['hotel_name', 'average_score']]
print(result)
