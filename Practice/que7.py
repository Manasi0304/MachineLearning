"""7. Write a program to do: A dataset collected in a cosmetics shop showing
details of customers and whether or not they responded to a special offer
to buy a new lip-stick is shown in table below. (Use library commands)
According to the decision tree you have made from the previous training
data set, what is the decision for the test data: [Age > 35, Income =
Medium, Gender = Female, Marital Status = Married]?"""

from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import LabelEncoder
import pandas as pd

# Load the dataset
df = pd.read_csv("Datasets/Lipstick.csv")
print("Dataset:\n", df)

# Test data
# test_data = {"Age": "<21", "Income": "Low", "Gender": "Female", "Ms": "Married"}
test_data = {"Age": ">35", "Income": "Medium", "Gender": "Female", "Ms": "Married"}
#test_data = {"Age": "21-35", "Income": "Low", "Gender": "Male", "Ms": "Married"}



# Encode categorical data to numerical using LabelEncoder
label_encoders = {}
for column in df.columns[1:]:  # Skip the "Id" column
    le = LabelEncoder()
    df[column] = le.fit_transform(df[column])
    label_encoders[column] = le

# Features and target variable
X = df.drop(["Id", "Buys"], axis=1)  # Exclude "Id" and "Buys"
y = df["Buys"]

# Train decision tree classifier
clf = DecisionTreeClassifier(criterion="entropy", random_state=42)
clf.fit(X, y)

# Encode test data using the same LabelEncoder
encoded_test = []
for col, value in test_data.items():
    if value in label_encoders[col].classes_:
        encoded_value = label_encoders[col].transform([value])[0]
    else:
        raise ValueError(f"Test data contains an unknown category for '{col}': '{value}'")
    encoded_test.append(encoded_value)

# Predict the outcome
prediction = clf.predict([encoded_test])
result = label_encoders["Buys"].inverse_transform(prediction)[0]
print("Decision for test data:",result)