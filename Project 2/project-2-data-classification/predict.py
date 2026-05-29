import pickle
import pandas as pd

# Load trained model
with open("models/iris_model.pkl", "rb") as file:
    model = pickle.load(file)

# Flower class names
flower_names = {
    0: "Setosa",
    1: "Versicolor",
    2: "Virginica"
}

# Sample input
# Format:
# [sepal length, sepal width, petal length, petal width]

sample = pd.DataFrame([[5.1, 3.5, 1.4, 0.2]], columns=[
    "sepal length (cm)",
    "sepal width (cm)",
    "petal length (cm)",
    "petal width (cm)"
])

# Predict
prediction = model.predict(sample)[0]

# Print result
print("\nFlower Prediction Result")
print("-" * 30)

print(f"Sepal Length : {sample.iloc[0,0]} cm")
print(f"Sepal Width  : {sample.iloc[0,1]} cm")
print(f"Petal Length : {sample.iloc[0,2]} cm")
print(f"Petal Width  : {sample.iloc[0,3]} cm")

print("\nPredicted Flower Class:", prediction)
print("Predicted Flower Name :", flower_names[prediction])

print("\nPrediction completed successfully.")