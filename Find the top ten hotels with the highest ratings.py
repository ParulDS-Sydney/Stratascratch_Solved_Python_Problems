import pandas as pd
unique_hotels = hotel_reviews['hotel_name', 'average_score'].drop_duplicates()
top_10_hotels = unique_hotels.sort_values(by='average_score', ascending=False).head(10)
print(top_10_hotels)
