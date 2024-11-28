""" 19. Write a Python program to display some basic statistical details like
percentile, mean, standard deviation etc (Use python and pandas
commands) the species of ‘Iris-setosa’, ‘Iris-versicolor’ and ‘Iris-versicolor’
of iris.csv dataset.
"""
# Import necessary libraries
# Import necessary libraries
import pandas as pd

# Load the Iris dataset (assuming the file is named 'iris.csv' and located in the current directory)
df = pd.read_csv('Datasets/IRIS.csv')

# Display basic info and the first few rows of the dataset
print("Dataset Info:")
print(df.info())
print("\nFirst 5 rows of the dataset:")
print(df.head())

# Filter the dataset by species
setosa = df[df['species'] == 'Iris-setosa']
versicolor = df[df['species'] == 'Iris-versicolor']
virginica = df[df['species'] == 'Iris-virginica']

# Basic statistical details for each species
# We will use the 'describe()' method, which computes percentiles, mean, std, etc.
print("\nBasic Statistical Details for Iris-setosa:")
print(setosa.describe())

print("\nBasic Statistical Details for Iris-versicolor:")
print(versicolor.describe())

print("\nBasic Statistical Details for Iris-virginica:")
print(virginica.describe())

# Additional Statistics: Percentiles (25th, 50th, 75th)
# Only apply quantiles on numeric columns (exclude 'species')
numeric_columns = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width']

print("\nAdditional Percentiles for Iris-setosa:")
print(setosa[numeric_columns].quantile([0.25, 0.5, 0.75]))

print("\nAdditional Percentiles for Iris-versicolor:")
print(versicolor[numeric_columns].quantile([0.25, 0.5, 0.75]))

print("\nAdditional Percentiles for Iris-virginica:")
print(virginica[numeric_columns].quantile([0.25, 0.5, 0.75]))

