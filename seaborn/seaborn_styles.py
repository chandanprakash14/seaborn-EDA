import numpy as np
import pandas as pd  # Updated alias
import matplotlib.pyplot as plt  # Updated alias
import seaborn as sns

# Set style
sns.set(style="darkgrid")

# Load the dataset
flights = sns.load_dataset("flights")

# Filter numeric columns only
numeric_flights = flights.select_dtypes(include=[np.number])

# Create a PairGrid
pair_grid = sns.PairGrid(numeric_flights)

# Map scatter plot to the grid
pair_grid.map(plt.scatter)

# Show the plot
plt.show()
