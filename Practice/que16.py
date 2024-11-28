""" 16. Use the inbuilt dataset 'titanic'. The dataset contains 891 rows and
contains information about the passengers who boarded the unfortunate
Titanic ship. Write a code to check how the price of the ticket (column
name: 'fare') for each passenger is distributed by plotting a histogram """

# Import necessary libraries
# Import necessary libraries
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Load the Titanic dataset from a local file
df = pd.read_csv("Datasets/Titanic.csv")

# Display basic information about the dataset
print("Dataset Info:")
print(df.info())
print("\nFirst 5 Rows of the Dataset:")
print(df.head())

# Plot a histogram to visualize the distribution of the 'Fare' column
plt.figure(figsize=(10, 6))
sns.histplot(data=df, x="Fare", kde=True, color="blue", bins=30)
plt.title("Distribution of Ticket Price (Fare)")
plt.xlabel("Fare")
plt.ylabel("Frequency")
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()
