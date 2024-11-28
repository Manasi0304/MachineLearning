""" 15. Use the dataset 'titanic'. The dataset contains 891 rows and contains
information about the passengers who boarded the unfortunate Titanic
ship. Use the Seaborn library to see if we can find any patterns in the data.
"""
# Import necessary libraries
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv("Datasets/Titanic.csv")

# Display basic info about the dataset
print("Dataset Info:")
print(df.info())
print("\nDataset Description:")
print(df.describe())
print("\nFirst 5 Rows:")
print(df.head())

# Set a seaborn theme for better visualization
sns.set_theme(style="whitegrid")

# 1. Survival rate by gender
plt.figure(figsize=(8, 6))
sns.countplot(data=df, x="Sex", hue="Survived", palette="Set2")
plt.title("Survival Rate by Gender")
plt.xlabel("Gender")
plt.ylabel("Count")
plt.legend(title="Survived", labels=["No", "Yes"])
plt.show()

# 2. Survival rate by passenger class
plt.figure(figsize=(8, 6))
sns.countplot(data=df, x="Pclass", hue="Survived", palette="Set1")
plt.title("Survival Rate by Passenger Class")
plt.xlabel("Passenger Class")
plt.ylabel("Count")
plt.legend(title="Survived", labels=["No", "Yes"])
plt.show()

# 3. Age distribution of passengers
plt.figure(figsize=(10, 6))
sns.histplot(data=df, x="Age", hue="Survived", kde=True, palette="coolwarm", bins=30)
plt.title("Age Distribution of Passengers")
plt.xlabel("Age")
plt.ylabel("Count")
plt.show()

# 4. Fare distribution by survival status
plt.figure(figsize=(10, 6))
sns.boxplot(data=df, x="Survived", y="Fare", palette="pastel")
plt.title("Fare Distribution by Survival Status")
plt.xlabel("Survived")
plt.ylabel("Fare")
plt.xticks([0, 1], ["No", "Yes"])
plt.show()

# 5. Correlation heatmap
plt.figure(figsize=(10, 8))
correlation_matrix = df.corr(numeric_only=True)
sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", fmt=".2f", square=True)
plt.title("Correlation Heatmap")
plt.show()

# 6. Survival rate by embarkation point
plt.figure(figsize=(8, 6))
sns.countplot(data=df, x="Embarked", hue="Survived", palette="viridis")
plt.title("Survival Rate by Embarkation Point")
plt.xlabel("Embarkation Point")
plt.ylabel("Count")
plt.legend(title="Survived", labels=["No", "Yes"])
plt.show()
