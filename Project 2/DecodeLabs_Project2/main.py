# ============================================================
#   DecodeLabs — Industrial Training Kit | Batch 2026
#   Project 2: Data Classification Using AI
#   Algorithm: K-Nearest Neighbors (KNN)
#   Dataset: Iris Benchmark
# ============================================================

# ─────────────────────────────────────────
# STEP 1: IMPORT LIBRARIES
# ─────────────────────────────────────────
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import (
    confusion_matrix,
    classification_report,
    f1_score,
    accuracy_score
)

import warnings
warnings.filterwarnings('ignore')

print("=" * 55)
print("   DecodeLabs | Project 2: Data Classification")
print("=" * 55)


# ─────────────────────────────────────────
# STEP 2: LOAD & UNDERSTAND THE DATASET
# ─────────────────────────────────────────
print("\n[STEP 1] Loading Iris Dataset...")

iris = load_iris()

# Convert to DataFrame for better understanding
df = pd.DataFrame(iris.data, columns=iris.feature_names)
df['species'] = iris.target
df['species_name'] = df['species'].map({
    0: 'Setosa',
    1: 'Versicolor',
    2: 'Virginica'
})

print("\n--- Dataset Overview ---")
print(f"Total Samples  : {df.shape[0]}")
print(f"Total Features : {df.shape[1] - 2}")
print(f"Classes        : {iris.target_names.tolist()}")

print("\n--- First 5 Rows ---")
print(df.head())

print("\n--- Dataset Statistics ---")
print(df.describe().round(2))

print("\n--- Class Distribution ---")
print(df['species_name'].value_counts())


# ─────────────────────────────────────────
# STEP 3: PREPARE FEATURES & TARGET
# ─────────────────────────────────────────
print("\n[STEP 2] Preparing Features and Target...")

X = iris.data    # Features (sepal/petal measurements)
y = iris.target  # Target (0=Setosa, 1=Versicolor, 2=Virginica)

print(f"Feature Matrix Shape : {X.shape}")
print(f"Target Vector Shape  : {y.shape}")


# ─────────────────────────────────────────
# STEP 4: FEATURE SCALING (GATEKEEPER RULE)
# ─────────────────────────────────────────
print("\n[STEP 3] Applying Feature Scaling (StandardScaler)...")

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

print("Before Scaling — Mean of feature 1:", round(X[:, 0].mean(), 3))
print("After  Scaling — Mean of feature 1:", round(X_scaled[:, 0].mean(), 3))
print("Scaling Done: Mean=0, Variance=1 ✓")


# ─────────────────────────────────────────
# STEP 5: TRAIN-TEST SPLIT (80/20)
# ─────────────────────────────────────────
print("\n[STEP 4] Splitting Data — 80% Train / 20% Test...")

X_train, X_test, y_train, y_test = train_test_split(
    X_scaled,
    y,
    test_size=0.2,
    random_state=42,
    shuffle=True        # Remove order bias
)

print(f"Training Samples : {len(X_train)}")
print(f"Testing Samples  : {len(X_test)}")


# ─────────────────────────────────────────
# STEP 6: FIND OPTIMAL K (ELBOW METHOD)
# ─────────────────────────────────────────
print("\n[STEP 5] Finding Optimal K Value...")

error_rates = []
k_range = range(1, 31)

for k in k_range:
    knn_temp = KNeighborsClassifier(n_neighbors=k)
    knn_temp.fit(X_train, y_train)
    preds_temp = knn_temp.predict(X_test)
    error = 1 - accuracy_score(y_test, preds_temp)
    error_rates.append(error)

# Find the best K
best_k = error_rates.index(min(error_rates)) + 1
print(f"Best K Found: {best_k} (Lowest Error Rate)")

# Plot K Optimization Graph
plt.figure(figsize=(10, 5))
plt.plot(k_range, error_rates, color='steelblue',
         linestyle='--', marker='o',
         markerfacecolor='orange', markersize=8)
plt.axvline(x=best_k, color='red', linestyle=':', label=f'Best K = {best_k}')
plt.title('Tuning the Engine: Choosing Optimal K', fontsize=14, fontweight='bold')
plt.xlabel('K Value')
plt.ylabel('Error Rate')
plt.legend()
plt.tight_layout()
plt.savefig('outputs/k_optimization.png', dpi=150)
plt.show()
print("Graph saved → outputs/k_optimization.png")


# ─────────────────────────────────────────
# STEP 7: TRAIN THE KNN MODEL
# ─────────────────────────────────────────
print(f"\n[STEP 6] Training KNN Model with K={best_k}...")

model = KNeighborsClassifier(n_neighbors=best_k)
model.fit(X_train, y_train)      # FIT: Memorize the map

print("Model Training Complete ✓")


# ─────────────────────────────────────────
# STEP 8: MAKE PREDICTIONS
# ─────────────────────────────────────────
print("\n[STEP 7] Making Predictions on Test Data...")

predictions = model.predict(X_test)   # PREDICT: Apply logic

print("\nSample Predictions vs Actual:")
print(f"{'Actual':<15} {'Predicted':<15} {'Result'}")
print("-" * 40)
for actual, pred in zip(y_test[:10], predictions[:10]):
    result = "✓ Correct" if actual == pred else "✗ Wrong"
    print(f"{iris.target_names[actual]:<15}"
          f"{iris.target_names[pred]:<15} {result}")


# ─────────────────────────────────────────
# STEP 9: OUTPUT VALIDATION
# ─────────────────────────────────────────
print("\n[STEP 8] Evaluating Model Performance...")

# --- Accuracy ---
accuracy = accuracy_score(y_test, predictions)
print(f"\nAccuracy : {accuracy * 100:.2f}%")

# --- F1 Score ---
f1 = f1_score(y_test, predictions, average='weighted')
print(f"F1 Score : {f1:.4f}")

# --- Classification Report ---
print("\n--- Classification Report ---")
print(classification_report(
    y_test, predictions,
    target_names=iris.target_names
))

# --- Confusion Matrix ---
cm = confusion_matrix(y_test, predictions)

plt.figure(figsize=(8, 6))
sns.heatmap(cm,
            annot=True,
            fmt='d',
            cmap='Blues',
            xticklabels=iris.target_names,
            yticklabels=iris.target_names,
            linewidths=1,
            linecolor='white')
plt.title('Confusion Matrix — KNN Classification', fontsize=14, fontweight='bold')
plt.ylabel('Actual Label', fontsize=12)
plt.xlabel('Predicted Label', fontsize=12)
plt.tight_layout()
plt.savefig('outputs/confusion_matrix.png', dpi=150)
plt.show()
print("Graph saved → outputs/confusion_matrix.png")


# ─────────────────────────────────────────
# STEP 10: TEST WITH CUSTOM NEW DATA
# ─────────────────────────────────────────
print("\n[STEP 9] Predicting a Brand New Sample...")

# Format: [sepal_length, sepal_width, petal_length, petal_width]
new_sample = [[5.1, 3.5, 1.4, 0.2]]   # Try changing these values!

# Scale the new sample using the SAME scaler
new_sample_scaled = scaler.transform(new_sample)

# Predict
result = model.predict(new_sample_scaled)
species = iris.target_names[result[0]]

print(f"Input  : Sepal={new_sample[0][0]}cm x {new_sample[0][1]}cm | "
      f"Petal={new_sample[0][2]}cm x {new_sample[0][3]}cm")
print(f"Predicted Species → {species.upper()} 🌸")


# ─────────────────────────────────────────
# FINAL SUMMARY
# ─────────────────────────────────────────
print("\n" + "=" * 55)
print("   PROJECT 2 COMPLETE — DECODELABS")
print("=" * 55)
print(f"  Dataset       : Iris (150 samples, 3 classes)")
print(f"  Algorithm     : K-Nearest Neighbors (K={best_k})")
print(f"  Scaler        : StandardScaler")
print(f"  Train/Test    : 80% / 20%")
print(f"  Accuracy      : {accuracy * 100:.2f}%")
print(f"  F1 Score      : {f1:.4f}")
print(f"  Outputs saved : outputs/")
print("=" * 55)