"""13. Use the covid_vaccine_statewise.csv dataset and perform the following
analytics.
a. Describe the dataset
b. Number of persons state wise vaccinated for first dose in India
c. Number of persons state wise vaccinated for second dose in India"""

import pandas as pd

# Step 1: Load the dataset
file_path = "Datasets/Covid Vaccine Statewise.csv"  # Update this path as per your folder structure
df = pd.read_csv(file_path)

# Step 2: Describe the dataset
print("Dataset Information:\n")
print(df.info())
print("\nDataset Description:\n")
print(df.describe(include="all"))

# Step 3: Handle missing or incorrect data
print("\nChecking for Missing Values:\n")
print(df.isnull().sum())

# Step 4: Filter relevant columns
# Assuming the dataset has columns like 'State', 'First Dose Administered', and 'Second Dose Administered'
columns_to_consider = ['State', 'First Dose Administered', 'Second Dose Administered']
df = df[columns_to_consider]

# Step 5: Group by 'State' to find the total doses administered
statewise_vaccination = df.groupby('State').sum()

# Step 6: Number of persons state-wise vaccinated for the first dose
print("\nState-wise Vaccination for First Dose:\n")
print(statewise_vaccination['First Dose Administered'])

# Step 7: Number of persons state-wise vaccinated for the second dose
print("\nState-wise Vaccination for Second Dose:\n")
print(statewise_vaccination['Second Dose Administered'])
