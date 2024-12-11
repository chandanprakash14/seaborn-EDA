import numpy as np
import pandas as ns
import matplotlib.pyplot as nlt
import seaborn as sns
a=sns.load_dataset("iris")
b=sns.FacetGrid(a,col="species")
b=map(nlt.hist,"sepal_length")
nlt.show()