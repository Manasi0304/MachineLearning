"""8. Write a program to do: A dataset collected in a cosmetics shop showing
details of customers and whether or not they responded to a special offer
to buy a new lip-stick is shown in table below. (Use library commands)
According to the decision tree you have made from the previous training
data set, what is the decision for the test data: [Age = 21-35, Income = Low,
Gender = Male, Marital Status = Married]?
"""
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import LabelEncoder

# Load the dataset

df = pd.read_csv("Datasets/Lipstick.csv")  # Assuming the data is in the first sheet

# Encode categorical features and the target variable
label_encoders = {}
encoded_data = df.copy()

for column in ['Age', 'Income', 'Gender', 'Ms', 'Buys']:
    label_encoders[column] = LabelEncoder()
    encoded_data[column] = label_encoders[column].fit_transform(df[column])

# Separate features (X) and target (y)
X = encoded_data[['Age', 'Income', 'Gender', 'Ms']]
y = encoded_data['Buys']

# Train the Decision Tree Classifier
clf = DecisionTreeClassifier(criterion='entropy', random_state=42)
clf.fit(X, y)

# Encode the test data: [Age = 21-35, Income = Low, Gender = Male, Marital Status = Married]
test_data = pd.DataFrame([{
    'Age': '21-35',
    'Income': 'Low',
    'Gender': 'Male',
    'Ms': 'Married'
}])

for column in test_data.columns:
    test_data[column] = label_encoders[column].transform(test_data[column])

# Predict the decision for the test data
prediction = clf.predict(test_data)

# Decode the prediction back to the original label
predicted_label = label_encoders['Buys'].inverse_transform(prediction)

# Output
print("Test Data:", test_data)
print("Predicted Decision:", predicted_label[0])
