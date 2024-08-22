# Loading in required libraries
import pandas as pd
import seaborn as sns
import numpy as np

# Start coding here!
nobelData = pd.read_csv("data/nobel.csv")


top_gender = nobelData.groupby("sex").size().idxmax()
print(top_gender)