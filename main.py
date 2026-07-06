import joblib
import numpy as np

# Load the trained model
try:
    model = joblib.load("model.pkl")
except FileNotFoundError:
    print("Error: model.pkl not found.")
    print("Please run train_model.py first.")
    exit()


def get_student_data():
    """Collect student details from the user."""
    print("\n===== Student Performance Prediction =====\n")

    study_hours = float(input("Enter Study Hours per Day: "))
    attendance = float(input("Enter Attendance Percentage: "))
    previous_marks = float(input("Enter Previous Marks: "))
    assignment_score = float(input("Enter Assignment Score: "))
    quiz_score = float(input("Enter Quiz Score: "))
    internal_assessment = float(input("Enter Internal Assessment Score: "))

    return np.array([[study_hours,
                      attendance,
                      previous_marks,
                      assignment_score,
                      quiz_score,
                      internal_assessment]])


def predict_result(student_data):
    """Predict student performance."""
    prediction = model.predict(student_data)

    print("\n========== Prediction Result ==========")

    if prediction[0] == "Pass":
        print("Student is likely to PASS.")
    else:
        print("Student is likely to FAIL.")

    print("=======================================\n")


def main():
    student_data = get_student_data()
    predict_result(student_data)


if __name__ == "__main__":
    main()
