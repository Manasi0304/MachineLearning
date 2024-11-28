""" 3. Perform the following operations using Python on the data set
House_Price Prediction dataset. Compute standard deviation, variance and
percentiles using separate commands, for each feature. Create a histogram
for each feature in the dataset to illustrate the feature distributions.  """
# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_csv('Datasets/House Data.csv')
print(df.head())

for columns in df . select_dtypes(include=['number']).columns:
    print(f"standard deviation :{df[columns].std()}")
    print(f"variance:{df[columns].var()}")
    print(f"mean:{df[columns].mean()}")
    print(f"median:{df[columns].median()}")
    print(f"mode{df[columns].mode()}")
    percentile=df[columns].quantile([0.25,0.50,0.75]).to_dict()
    print(f"25th percentile: {percentile[0.25]}")
    print(f"50th percentile: {percentile[0.5]}")
    print(f"75th percentile: {percentile[0.75]}")

# Create histograms for each numerical feature using Seaborn
numerical_columns = df.select_dtypes(include=['number']).columns  # Get numerical columns

for i in df.columns:
    sns.histplot(df[i],kde=True,color='blue',bins=20)
    plt.xlabel(i)
    plt.ylabel('frequency')
    plt.title(f'Histogram of {i}')
    plt.show()