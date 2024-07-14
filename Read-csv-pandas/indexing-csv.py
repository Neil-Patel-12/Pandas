import pandas as pd
"""
Indexing means selecting specific rows and columns of data
from DataFrame. A DataFrame includes columns, index, and data.
1. Indexing in Pandas using the indexing operator []
2. Indexing in Pandas using loc[]
3. Indexing in Pandas using iloc[]
"""

df = pd.read_csv("C:\\Users\\neilp\\Desktop\\student.csv", index_col="Student")

print(df, "\n")

# indexing operator
res = df["Marks"]
print(res, "\n")

# retrieve a single row
row = df.loc["Amit"]
print(row, "\n")

# Retrieve row 3 records
getter = df.iloc[2]
print(getter, "\n")

