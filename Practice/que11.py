""" 11. Use Iris flower dataset and perform following :
1. List down the features and their types (e.g., numeric, nominal)
available in the dataset. 2. Create a histogram for each feature in the
dataset to illustrate the feature distributions.
"""
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the Iris dataset (assuming it's available in your environment)
# Replace 'iris.csv' with the actual file path if needed
try:
    iris_df = pd.read_csv('Datasets/IRIS.csv')  # Try loading from a CSV file
except FileNotFoundError:
    from sklearn import datasets
    iris = datasets.load_iris()
    iris_df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
    iris_df['species'] = iris.target_names[iris.target]


# 1. Features and their types
print("Features and their types:")
for col in iris_df.columns:
    if col == 'species':
        print(f"- {col}: Nominal (Categorical)")
    else:
        print(f"- {col}: Numeric (Continuous)")

# 2. Histograms for each feature
plt.figure(figsize=(12, 8))

for i, col in enumerate(iris_df.columns[:-1]):  # Exclude 'species'
    plt.subplot(2, 2, i + 1)
    sns.histplot(iris_df[col], kde=True)  # Use seaborn for better-looking histograms
    plt.title(f'Distribution of {col}')
    plt.xlabel(col)
    plt.ylabel('Frequency')

plt.tight_layout()
plt.show()


