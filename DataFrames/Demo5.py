# Iterate a Pandas DataFrame

import pandas as pd

# Dataset
data = {
    'Student': ['Amit', 'Michal', 'John', 'Smith', 'Milly'],
    'Rank': [1, 4, 3, 5, 2],
    'Marks': [95, 70, 80, 60, 90]
}

df = pd.DataFrame(data, index=['student1', 'student2', 'student3', 'student4', 'student5'])

print("student records\n\n", df)

# Iterating
print("\nDisplaying the columns:")
for col in df:
    print(col)