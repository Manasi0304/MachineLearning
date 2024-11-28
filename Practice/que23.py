""" 23. With reference to Table , obtain the Frequency table for the
attribute age. From the frequency table you have obtained, calculate the
information gain of the frequency table while splitting on Age. (Use step
by step Python/Pandas commands) """
import pandas as pd
import numpy as np

# Step 1: Creating the dataset as per the table in the image
data = {
    'Age': ['Young', 'Young', 'Middle', 'Old', 'Old', 'Old', 'Middle', 'Young', 'Young', 'Old', 'Young', 'Middle', 'Middle', 'Old'],
    'Income': ['High', 'High', 'High', 'Medium', 'Low', 'Low', 'Medium', 'Low', 'Medium', 'Medium', 'High', 'Medium', 'Medium', 'Medium'],
    'Married': ['No', 'No', 'No', 'Yes', 'Yes', 'Yes', 'No', 'No', 'Yes', 'Yes', 'No', 'Yes', 'No', 'Yes'],
    'Health': ['Fair', 'Good', 'Fair', 'Fair', 'Fair', 'Good', 'Fair', 'Fair', 'Fair', 'Fair', 'Good', 'Good', 'Good', 'No'],
    'Class': ['No', 'No', 'Yes', 'Yes', 'No', 'No', 'Yes', 'No', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'No']
}

df = pd.DataFrame(data)

# Step 2: Frequency table for 'Age'
frequency_table = df['Age'].value_counts()
print("Frequency Table for 'Age':")
print(frequency_table)

# Step 3: Calculate total entropy of the dataset
def calculate_entropy(series):
    probabilities = series.value_counts() / len(series)
    entropy = -np.sum(probabilities * np.log2(probabilities))
    return entropy

total_entropy = calculate_entropy(df['Class'])
print("\nTotal Entropy of the dataset:")
print(total_entropy)

# Step 4: Calculate the entropy for each group of 'Age'
age_groups = df.groupby('Age')
weighted_entropy = 0

print("\nEntropy for each 'Age' group:")
for age, group in age_groups:
    group_entropy = calculate_entropy(group['Class'])
    weight = len(group) / len(df)
    weighted_entropy += weight * group_entropy
    print(f"Age = {age}, Entropy = {group_entropy:.4f}, Weight = {weight:.4f}")

# Step 5: Calculate information gain
information_gain = total_entropy - weighted_entropy
print("\nInformation Gain for splitting on 'Age':")
print(information_gain)
