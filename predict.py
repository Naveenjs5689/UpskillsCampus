import joblib
import pandas as pd

# -----------------------------
# Load Trained Model
# -----------------------------
try:
    model = joblib.load("model.pkl")
except FileNotFoundError:
    print("Error: model.pkl not found!")
    print("Please run train_model.py first.")
    exit()

print("Student Performance Prediction System")
print("-" * 40)

# -----------------------------
# Get User Input
# -----------------------------
study_hours = float(input("Enter Study Hours per Day: "))
attendance = float(input("Enter Attendance (%): "))
previous_marks = float(input("Enter Previous Marks: "))
assignment_score = float(input("Enter Assignment Score: "))
quiz_score = float(input("Enter Quiz Score: "))
internal_assessment = float(input("Enter Internal Assessment Score: "))

# -----------------------------
# Create DataFrame
# -----------------------------
student_data = pd.DataFrame({
    "Study_Hours": [study_hours],
    "Attendance": [attendance],
    "Previous_Marks": [previous_marks],
    "Assignment_Score": [assignment_score],
    "Quiz_Score": [quiz_score],
    "Internal_Assessment": [internal_assessment]
})

# -----------------------------
# Predict Result
# -----------------------------
prediction = model.predict(student_data)[0]

print("\nPrediction Result")
print("-" * 40)

if prediction == "Pass":
    print("The student is likely to PASS.")
else:
    print("The student is likely to FAIL.")

# -----------------------------
# Prediction Confidence
# -----------------------------
if hasattr(model, "predict_proba"):
    probabilities = model.predict_proba(student_data)[0]

    print("\nPrediction Confidence")
    print("-" * 40)

    for label, probability in zip(model.classes_, probabilities):
        print(f"{label}: {probability * 100:.2f}%")
