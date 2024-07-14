# create  a Pandas DataFrame

import pandas as pd

data = {
    'Student': ['Amit', 'Michal', 'John', 'Smith', 'Milly'],
    'Rank': [1, 2, 3, 4, 5],
    'Marks': [95, 70, 80, 60, 90]
}

df = pd.DataFrame(data)

print("student records\n\n", df)