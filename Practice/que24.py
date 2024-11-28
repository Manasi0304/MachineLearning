""" 24. Perform the following operations using Python on a suitable data set,
counting unique values of data, format of each column, converting variable
data type (e.g. from long to short, vice versa), identifying missing values
and filling in the missing values.
"""
import pandas as pd
import numpy as np

# Step 1: Creating a sample dataset
data = {
    "ID": [1, 2, 3, 4, 5],
    "Name": ["Alice", "Bob", "Charlie", "David", np.nan],
    "Age": [25, 30, np.nan, 22, 28],
    "Salary": [50000.0, 54000.5, 58000.3, np.nan, 62000.0],
    "JoiningDate": ["2020-01-15", "2019-11-10", "2021-05-12", "2022-02-20", "2023-03-25"]
}

df = pd.DataFrame(data)

print("Original Dataset:")
print(df)

# Step 2: Count unique values in each column
unique_counts = df.nunique()
print("\nCount of unique values in each column:")
print(unique_counts)

# Step 3: Get the format (data type) of each column
data_types = df.dtypes
print("\nData types of each column:")
print(data_types)

# Step 4: Convert variable data type (e.g., from string to datetime)
df['JoiningDate'] = pd.to_datetime(df['JoiningDate'])
print("\nConverted 'JoiningDate' to datetime:")
print(df.dtypes)

# Step 5: Identify missing values
missing_values = df.isnull().sum()
print("\nMissing values in each column:")
print(missing_values)

# Step 6: Fill in missing values
# Filling missing 'Name' with 'Unknown'
df['Name'] = df['Name'].fillna("Unknown")
# Filling missing 'Age' with the mean age
df['Age'] = df['Age'].fillna(df['Age'].mean())
# Filling missing 'Salary' with the median salary
df['Salary'] = df['Salary'].fillna(df['Salary'].median())

print("\nDataset after filling missing values:")
print(df)

# Step 7: Convert numeric column (e.g., ID) from int to float and back to int
df['ID'] = df['ID'].astype(float)  # Convert to float
print("\nConverted 'ID' to float:")
print(df.dtypes)

df['ID'] = df['ID'].astype(int)  # Convert back to int
print("\nConverted 'ID' back to int:")
print(df.dtypes)
