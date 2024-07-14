# series in Pandas is a one-dimensional array, like a column in a table.
# It is a labeled array that can hold data of any type.
# The Series() method is used for this and has the following parameters:
# data, index, dtype, name, copy

import pandas as pd

data = [10, 20, 40, 80, 100]

# Create a Series using the method
s = pd.Series(data)

print("Series = ")
print(s)

# access a value from a pandas series
print("\nValue at index 2 is", s[2])

# Name your INDEXes in pandas series
data2 = ["apple", "banana", "cherry", "grapes", "watermelon"]
s2 = pd.Series(data2, index=['f1', 'f2', 'f3', 'f4', 'f5'])
print("\nindex = \n", s2)
print("\nValue at index 1 is:", s2["f1"])