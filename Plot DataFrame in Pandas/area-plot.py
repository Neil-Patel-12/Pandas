# Area plot in Python Pandas

import pandas as pd
import matplotlib.pyplot as plt

# DataSet
data = {
    'Temperature': [18, 20, 22, 19, 23, 24, 28, 26, 17, 25],
    'Humidity': [32, 31, 30, 22, 17, 29, 32, 37, 20, 19],
    'Wind': [12, 20, 8, 9, 20, 27, 22, 33, 37, 35],
    'Precipitation': [17, 25, 20, 19, 18, 20, 28, 26, 29, 22]
}

df = pd.DataFrame(data)

# Area Plot
df.plot.area()

# Display the figure
plt.show()