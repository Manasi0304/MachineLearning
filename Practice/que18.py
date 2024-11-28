""" 18. Use House_Price prediction dataset. Provide summary statistics (mean,
median, minimum, maximum, standard deviation) of variables (categorical
vs quantitative) such as- For example, if categorical variable is age groups
and quantitative variable is income, then provide summary statistics of
income grouped by the age groups. """

# Importing necessary libraries
import pandas as pd

# Load the dataset (assuming the file is named 'House_Price.csv' and located in the 'Datasets' folder)
df = pd.read_csv('Datasets/House Data.csv')

# Display basic info and the first few rows of the dataset
print("Dataset Info:")
print(df.info())
print("\nFirst 5 rows of the dataset:")
print(df.head())

# Example: Categorical variable is 'Neighborhood', and quantitative variable is 'SalePrice'
# Group by categorical variable ('Neighborhood') and compute summary statistics for 'SalePrice'
summary_stats = df.groupby('Neighborhood')['SalePrice'].describe()

# To get the specific statistics (mean, median, min, max, std)
mean_values = df.groupby('Neighborhood')['SalePrice'].mean()
median_values = df.groupby('Neighborhood')['SalePrice'].median()
min_values = df.groupby('Neighborhood')['SalePrice'].min()
max_values = df.groupby('Neighborhood')['SalePrice'].max()
std_values = df.groupby('Neighborhood')['SalePrice'].std()

# Print the summary statistics for each group
print("\nSummary Statistics of 'SalePrice' grouped by 'Neighborhood':")
print("Mean:")
print(mean_values)
print("\nMedian:")
print(median_values)
print("\nMinimum:")
print(min_values)
print("\nMaximum:")
print(max_values)
print("\nStandard Deviation:")
print(std_values)

# Alternatively, you can also view the full describe method output for a better overview:
print("\nFull Summary Statistics using 'describe()' method:")
print(summary_stats)
