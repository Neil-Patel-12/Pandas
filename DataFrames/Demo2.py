# Access group of rows or columns in a Pandas DataFrame

import pandas as pd

# Dataset
data = {
    'Student': ['Amit', 'Michal', 'John', 'Smith', 'Milly'],
    'Rank': [1, 2, 3, 4, 5],
    'Marks': [95, 70, 80, 60, 90]
}

df = pd.DataFrame(data, index=['RowA', 'RowB', 'RowC', 'RowD', 'RowE'])

print("student records\n\n", df)

# Access the value in the student column corresponding to the RowA label
print("\nValue =", df.loc['RowA', 'Student'])