# Name your indexes in a Pandas DataFrame

import pandas as pd

# Dataset
data = {
    'Student': ['Amit', 'Michal', 'John', 'Smith', 'Milly'],
    'Rank': [1, 4, 3, 5, 2],
    'Marks': [95, 70, 80, 60, 90]
}

# Use the index argument to set your indexes
df = pd.DataFrame(data, index=['student1', 'student2', 'student3', 'student4', 'student5'])

print("student records\n\n", df)