import numpy as np
import pandas as ns
import matplotlib.pyplot as nlt
import seaborn as sns
a=sns.load_dataset("tips")
sns.catplot(x="time",y="tip",data=a)
nlt.show()