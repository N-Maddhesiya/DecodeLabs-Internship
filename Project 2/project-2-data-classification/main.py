import os
import pickle
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# Create folders if they do not exist
os.makedirs("data", exist_ok=True)
os.makedirs("models", exist_ok=True)
os.makedirs("outputs", exist_ok=True)

# Load dataset
iris = load_iris(as_frame=True)
df = iris.frame

# Save dataset as CSV for project submission
df.to_csv("data/iris.csv", index=False)

# Load CSV file
data = pd.read_csv("data/iris.csv")

print("First 5 rows:")
print(data.head())

print("\nDataset information:")
print(data.info())

print("\nMissing values:")
print(data.isnull().sum())

# Separate features and target
X = data.drop("target", axis=1)
y = data["target"]

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train model
model = DecisionTreeClassifier(random_state=42)
model.fit(X_train, y_train)

# Predict
y_pred = model.predict(X_test)

# Evaluate
accuracy = accuracy_score(y_test, y_pred)
report = classification_report(y_test, y_pred)
matrix = confusion_matrix(y_test, y_pred)

print("\nAccuracy:", accuracy)
print("\nClassification Report:\n", report)
print("\nConfusion Matrix:\n", matrix)

# Save model
with open("models/iris_model.pkl", "wb") as file:
    pickle.dump(model, file)

# Save results
with open("outputs/result.txt", "w") as file:
    file.write(f"Accuracy: {accuracy}\n\n")
    file.write("Classification Report:\n")
    file.write(report)
    file.write("\nConfusion Matrix:\n")
    file.write(str(matrix))

print("\nModel saved successfully in models/iris_model.pkl")