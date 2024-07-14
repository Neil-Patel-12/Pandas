# join DataFrame in Pandas

import pandas as pd

# Datasets
data1 = {
    'Id': ['SO1', 'SO2', 'SO3', 'SO4', 'SO5', 'SO6'],
    'Student': ['Amit', 'Michal', 'John', 'Nathan', 'David', 'Steve'],
    'Roll': [101, 102, 103, 104, 105, 106]
}
data2 = {
    'Rank': [1, 4, 3, 5, 2, 6],
    'Marks': [10, 20, 30, 40, 50, 60]
}

df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)

print('\nDataFrame1\n', df1)
print('\nDataFrame2\n', df2)

# Join 2 data frames
resDF = df1.join(df2)
print('\nJoined DataFrame\n', resDF)
