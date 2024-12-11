import numpy as np
import pandas as pd  # Updated alias
import matplotlib.pyplot as plt  # Updated alias
import seaborn as sns
sns.set(style="darkgrid")
flights = sns.load_dataset("flights")
numeric_flights = flights.select_dtypes(include=[np.number])
pair_grid = sns.PairGrid(numeric_flights)
pair_grid.map(plt.scatter)
plt.show()
