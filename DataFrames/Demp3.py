# Access a group of rows or columns by integer positions in a Pandas DataFrame

import pandas as pd

# Dataset
data = {
    'Student': ['Amit', 'Michal', 'John', 'Smith', 'Milly'],
    'Rank': [1, 4, 3, 5, 2],
    'Marks': [95, 70, 80, 60, 90]
}

df = pd.DataFrame(data, index=['RowA', 'RowB', 'RowC', 'RowD', 'RowE'])

print("student records\n\n", df)

# Access using rows or columns by integer positions
print("\nValue = \n", df.iloc[[1, 2]])