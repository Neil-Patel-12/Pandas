# series in pandas comes with many attributes and methods
import pandas as pd
import numpy as np
# Attributes:
"""
    dtype - return the dtype,
    ndim - return the number of dimensions,
    size - return the number of elements,
    name - return the name of the series,
    hasnans - return True if NaNs are in the series,
    index - the index of the series
"""

# Methods:
"""
    head() - return the first n rows, 
    tail() - return the last n rows, 
    info() - display the summary of the series
"""

data = [10, 20, 40, 80, 100, np.nan]
s = pd.Series(data, name="MyNumberSeries")

print(s, "\n")

print("Series Data Type:", s.dtype, "\n")

print("Dimension:", s.ndim, "\n")

print("Size:", s.size, "\n")

print("Name:", s.name, "\n")

print("Contains NaN:", s.hasnans, "\n")

print("Indexes:", s.index, "\n")

print("Head\n", s.head(2), "\n")
print("Tail\n", s.tail(2), "\n")
print("Info:", s.info(), "\n")