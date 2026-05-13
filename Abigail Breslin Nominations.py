import pandas as pd

abigail_nominations = oscar_nominees[oscar_nominees['nominee'] == 'Abigail Breslin']

# Count the number of unique movies
movie_count = abigail_nominations['movie'].nunique()

print(f"Number of movies: {movie_count}")
