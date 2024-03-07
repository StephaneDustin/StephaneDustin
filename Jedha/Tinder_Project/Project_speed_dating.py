import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly as pl
df = pd.read_csv("Speed_data.csv", encoding = "unicode_escape")
print(df.head())
df_1 = df.dropna(axis=0, how="all", inplace= True)
print (df_1.head())
print (len(df)-len(df_1))
print (len(df))