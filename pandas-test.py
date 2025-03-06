import pandas as pd

#Sample DataFrame
data = {'A': [1, 2, 3, 4, 5],
        'B': ['a', 'b', 'c', 'd', 'e'],
        'C': ['prashant', 'hi', 'test','s','mytest']}
df = pd.DataFrame(data)
filtered_df = df[df['C'].str.len() > 3]
print(filtered_df)