import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# -----------------------------
# Load Dataset
# -----------------------------
data = pd.read_csv("dataset.csv")

print("Dataset Loaded Successfully!\n")

# -----------------------------
# Display Dataset Information
# -----------------------------
print("First 5 Rows:")
print(data.head())

print("\nDataset Shape:", data.shape)

# -----------------------------
# Feature Selection
# -----------------------------
X = data[[
    "Study_Hours",
    "Attendance",
    "Previous_Marks",
    "Assignment_Score",
    "Quiz_Score",
    "Internal_Assessment"
]]

y = data["Final_Result"]

# -----------------------------
# Split Dataset
# -----------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42
)

# -----------------------------
# Train Model
# -----------------------------
model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(X_train, y_train)

print("\nModel Training Completed Successfully!")

# -----------------------------
# Predictions
# -----------------------------
y_pred = model.predict(X_test)

# -----------------------------
# Evaluation
# -----------------------------
accuracy = accuracy_score(y_test, y_pred)

print("\nModel Accuracy: {:.2f}%".format(accuracy * 100))

print("\nClassification Report")
print(classification_report(y_test, y_pred))

print("\nConfusion Matrix")
print(confusion_matrix(y_test, y_pred))

# -----------------------------
# Save Model
# -----------------------------
joblib.dump(model, "model.pkl")

print("\nTrained model saved as model.pkl")

# -----------------------------
# Sample Prediction
# -----------------------------
sample = [[6, 90, 82, 85, 84, 83]]

prediction = model.predict(sample)

print("\nSample Prediction:")

if prediction[0] == "Pass":
    print("Student is likely to PASS.")
else:
    print("Student is likely to FAIL.")
