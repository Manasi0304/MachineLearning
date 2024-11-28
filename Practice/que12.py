""" 12.Use Iris flower dataset and perform following :
1. Create a box plot for each feature in the dataset.
2. Identify and discuss distributions and identify outliers from them.
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Step 1: Load the Iris dataset
file_path = "Datasets/IRIS.csv"  # Update this path to match your folder structure
df = pd.read_csv(file_path)

# Step 2: Drop unnecessary columns if present (like 'Id')
if 'Id' in df.columns:
    df = df.drop(columns=['Id'])

# Step 3: Display basic information
print("Dataset Information:\n")
print(df.info())
print("\nDataset Description:\n")
print(df.describe())

# Step 4: Create box plots for each feature
features = df.columns[:-1]  # Exclude the target column ('Species')

plt.figure(figsize=(12, 8))
for i, feature in enumerate(features, 1):
    plt.subplot(2, 2, i)  # Create subplots for better visualization
    sns.boxplot(y=feature, data=df)
    plt.title(f"Box Plot of {feature}")
plt.tight_layout()
plt.show()

# Step 5: Discuss distributions and identify outliers
print("\nOutlier Analysis:")
for feature in features:
    q1 = df[feature].quantile(0.25)  # First quartile (25th percentile)
    q3 = df[feature].quantile(0.75)  # Third quartile (75th percentile)
    iqr = q3 - q1  # Interquartile range
    lower_bound = q1 - 1.5 * iqr
    upper_bound = q3 + 1.5 * iqr
    outliers = df[(df[feature] < lower_bound) | (df[feature] > upper_bound)]
    print(f"{feature} - Outliers:\n{outliers[[feature, 'Species']]}")  # Display feature and species for outliers

