import pandas as pd

df = pd.read_csv(r'data\hacker_news.csv')

first_5_rows = df.head()
# print(first_5_rows)

last_5_rows = df.tail()
# print(last_5_rows)

title_series = df.iloc[:,2]
# print(title_series)

# print(df.shape)

python_title = df.loc[df['title'].str.contains('Python', case=False)]
# print(python_title)

js_title = df.loc[df['title'].str.contains('JavaScript', case=False)]
# print(js_title)

# print(df.describe())