"""14. Use the covid_vaccine_statewise.csv dataset and perform the following
analytics.
A. Describe the dataset.
B. Number of Males vaccinated
C.. Number of females vaccinated """

import pandas as pd

# Step 1: Load the dataset
file_path = "Datasets/Covid Vaccine Statewise.csv"  # Update this path to match your folder structure
df = pd.read_csv(file_path)

# Step 2: Describe the dataset
print("Dataset Information:\n")
print(df.info())
print("\nDataset Description:\n")
print(df.describe(include="all"))

# Step 3: Check for missing values
print("\nChecking for Missing Values:\n")
print(df.isnull().sum())

# Step 4: Filter relevant columns
# Assuming the dataset has columns like 'Male (Doses Administered)' and 'Female (Doses Administered)'
columns_to_consider = ['State', 'Male (Doses Administered)', 'Female (Doses Administered)']
df = df[columns_to_consider]

# Convert columns to numeric (if necessary) to handle non-numeric or missing values
df['Male (Doses Administered)'] = pd.to_numeric(df['Male (Doses Administered)'], errors='coerce')
df['Female (Doses Administered)'] = pd.to_numeric(df['Female (Doses Administered)'], errors='coerce')

# Step 5: Total number of males and females vaccinated
total_males_vaccinated = df['Male (Doses Administered)'].sum()
total_females_vaccinated = df['Female (Doses Administered)'].sum()

# Display the results
print(f"\nTotal Number of Males Vaccinated: {total_males_vaccinated}")
print(f"Total Number of Females Vaccinated: {total_females_vaccinated}")
