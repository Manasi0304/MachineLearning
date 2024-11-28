""" 2. Perform the following operations using Python on the Telecom_Churn
dataset. Compute and display summary statistics for each feature available
in the dataset using separate commands for each statistic. (e.g. minimum
value, maximum value, mean, range, standard deviation, variance and
percentiles)."""
# Import necessary libraries
import pandas as pd
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

df= pd.read_csv('Datasets/Telecom Churn.csv')
print(df.head())
print(df.info())
# Compute and display summary statistics for each feature available in the dataset
for column in df.select_dtypes(include=['number']).columns:
    print(f"Summary statistics for {column}:")
    print(f"Minimum value: {df[column].min()}")
    print(f"Maximum value: {df[column].max()}")
    print(f"Mean: {df[column].mean()}")
    print(f"Range: {df[column].max()}-{df[column].min()}")
    print(f"Standard Deviation: {df[column].std()}")
    print(f"Variance: {df[column].var()}")
    #percentile
    percentiles = df[column].quantile([0.25, 0.5, 0.75]).to_dict()
    print(f"25th percentile: {np.percentile(df[column], 25)}")
    print(f"50th percentile: {np.percentile(df[column], 50)}")
    print(f"75th percentile: {np.percentile(df[column], 75)}")
