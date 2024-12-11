import numpy as np
import pandas as ns
import matplotlib.pyplot as nlt
import seaborn as sns
a=sns.load_dataset("flights")
sns.relplot(x="passengers",y="month",hue='year',data=a)
'''nlt.title("Regression Plot of Passengers vs. Month")
nlt.xlabel("Passengers")
nlt.ylabel("Month (Numerical)")'''
nlt.show()