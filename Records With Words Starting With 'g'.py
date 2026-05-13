import pandas as pd
condition=(google_word_lists['words1'].str.startswith('g',na=False))| (google_word_lists['words2'].str.startswith('g',na=False))
result=google_word_lists[condition]
print(result)
