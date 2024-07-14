import pandas as pd

"""
select multiple columns in Pandas DataFrame
1. Select two columns
  -> to select 2 col in pandas DF, mention the col name
  -> dataFrame[['Rank', 'Marks']]
2. select multiple columns in a range
  -> mention index number in a range separated by a colon
"""

path = "C:\\Users\\neilp\\Desktop\\student.csv"
df = pd.read_csv(path)

print(df[['Student', 'Marks']], "\n")

# this will select all columns in a range
print(df[df.columns[0:2]])