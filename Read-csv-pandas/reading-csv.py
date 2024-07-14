import pandas as pd

"""
Read CSV in Pandas:
1. Read a CSV
2. Display the top n rows of the DataFrame
3. Display the last n rows of the DataFrame
"""

path = "C:\\Users\\neilp\\Desktop\\student.csv"
df = pd.read_csv(path)

print(df)