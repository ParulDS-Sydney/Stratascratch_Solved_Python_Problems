import pandas as pd
words_series = google_file_store['contents'].str.split().explode()
word_counts = words_series.value_counts().reset_index()
word_counts.columns = ['word', 'occurrences']
print(word_counts)
