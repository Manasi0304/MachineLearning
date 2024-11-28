import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import LabelEncoder

# Step 1: Load the dataset
df = pd.read_csv("Datasets/Lipstick.csv")

# Step 2: Encode categorical values using LabelEncoders for each column
label_encoders = {}  # Dictionary to store encoders for each column
for col in ['Age', 'Income', 'Gender', 'Ms']:
    le = LabelEncoder()
    df[col] = le.fit_transform(df[col])
    label_encoders[col] = le  # Save the LabelEncoder for future use

# Step 3: Prepare features X and target Y
X = df[['Age', 'Income', 'Gender', 'Ms']]
Y = df['Buys']

# Step 4: Train DecisionTreeClassifier
clf = DecisionTreeClassifier(criterion='entropy', random_state=42)
clf.fit(X, Y)

# Step 5: Create test data
test_data = pd.DataFrame([{
    'Age': label_encoders['Age'].transform(['>35'])[0],
    'Income': label_encoders['Income'].transform(['Medium'])[0],
    'Gender': label_encoders['Gender'].transform(['Female'])[0],
    'Ms': label_encoders['Ms'].transform(['Married'])[0]
}])

# Step 6: Predict using the trained model
prediction = clf.predict(test_data)

# Step 7: Output the result
# Assuming "Yes" is encoded as 0 and "No" as 1; adjust if reversed
if prediction[0] == 0:
    print("The customer will respond to the offer (Yes).")
else:
    print("The customer will not respond to the offer (No).")
