# Pandas DataFrame dtypes attribute

import pandas as pd

data = {
    'Student': ['Amit', 'Michal', 'John', 'Nathan', 'David', 'Steve'],
    'Rank': [1, 4, 3, 5, 2, 6],
    'Marks': [95, 70, 80, 60, 90, 87]
}

# Create a DataFrame using the DataFrame() method with index
df = pd.DataFrame(data, index=['RowA', 'RowB', 'RowC', 'RowD', 'RowE', 'RowF'])

print("student records\n\n", df)

# return the data types
print("\nDatatypes:\n", df.dtypes)

# return the number of dimensions in the DataFrame
print("\nNumber of Dimensions:\n", df.ndim)

# return the number of elements in the DataFrame
print("\nsize:\n", df.size)

# return the dimensionality of the DataFrame in a tuple form
print("\nshape:\n", df.shape)

# return all the indexes
print("\nindex:\n", df.index)

# show the transpose table
print("\nTranspose:\n", df.T)

# return the first n rows default=5
print("\nHead\n", df.head(4))

# return the las n rows
print("\nTail\n", df.tail(3))