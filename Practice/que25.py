""" 25. Perform Data Cleaning, Data transformation using Python on any data
set. """
import pandas as pd
from sklearn.preprocessing import StandardScaler
import numpy as np

# Step 1: Load the Iris dataset
# Assuming the Iris dataset is in the 'dataset' folder. Update the path if necessary.
df = pd.read_csv('Datasets/IRIS.csv')

# Display the first few rows of the dataset
print("Original Dataset:")
print(df.head())

# Step 2: Data Cleaning

# Check for missing values
missing_values = df.isnull().sum()
print("\nMissing values in each column:")
print(missing_values)

# Check for duplicate rows
duplicates = df.duplicated().sum()
print("\nNumber of duplicate rows:", duplicates)

# If there are missing values in numerical columns, fill with the mean
df.fillna(df.select_dtypes(include=[np.number]).mean(), inplace=True)

# If there are any duplicates, remove them
df.drop_duplicates(inplace=True)

# Step 3: Data Transformation

# Separate numerical and categorical columns
numerical_columns = df.select_dtypes(include=[np.number]).columns
categorical_columns = df.select_dtypes(exclude=[np.number]).columns

# 3.1: Feature Scaling (Standardization)
# Standardizing the numerical columns to have a mean of 0 and variance of 1
scaler = StandardScaler()
df[numerical_columns] = scaler.fit_transform(df[numerical_columns])

# 3.2: Encoding categorical variables
# Map the 'species' column to numeric values
df['species'] = df['species'].map({'setosa': 0, 'versicolor': 1, 'virginica': 2})

# Display the cleaned and transformed data
print("\nTransformed Data:")
print(df.head())

# Step 4: Saving the cleaned and transformed data (optional)
df.to_csv('Datasets/iris_cleaned_transformed.csv', index=False)

print("\nData cleaning and transformation complete. The cleaned data is saved.")
