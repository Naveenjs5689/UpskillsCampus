# UpskillsCampus
# Student Performance Prediction Using Machine Learning with Python

## 📌 Project Overview
The **Student Performance Prediction Using Machine Learning with Python** project predicts a student's academic performance based on various factors such as study hours, attendance, previous marks, assignment scores, and quiz scores. The project leverages machine learning algorithms to analyze historical student data and classify students based on their expected performance.

This system helps educational institutions identify students who may require additional academic support and enables data-driven decision-making to improve learning outcomes.

---

## 🎯 Objectives

- Predict student academic performance using machine learning.
- Analyze and preprocess educational datasets.
- Train and evaluate multiple machine learning models.
- Compare model performance using evaluation metrics.
- Visualize data and prediction results.
- Save the trained model for future predictions.

---

## 🛠 Technologies Used

- Python 3.x
- Pandas
- NumPy
- Matplotlib
- Scikit-learn
- Joblib

---

## 📂 Project Structure

```
upskillCampus/
│
├── code/
│   ├── dataset.csv
│   ├── train_model.py
│   ├── predict.py
│   ├── main.py
│   └── requirements.txt
│
├── report/
│   └── Final_Report.pdf
│
└── README.md
```

---

## 📊 Dataset Features

| Feature | Description |
|----------|-------------|
| Student_ID | Unique student identifier |
| Study_Hours | Average study hours per day |
| Attendance | Attendance percentage |
| Previous_Marks | Marks obtained in previous examination |
| Assignment_Score | Assignment marks |
| Quiz_Score | Quiz marks |
| Internal_Assessment | Internal assessment score |
| Final_Result | Target variable (Pass/Fail or Grade) |

---

## 🤖 Machine Learning Algorithms

The following algorithms can be used and compared:

- Logistic Regression
- Decision Tree Classifier
- Random Forest Classifier
- Support Vector Machine (SVM)

The **Random Forest Classifier** is recommended because it generally provides better prediction accuracy for this dataset.

---

## 📈 Project Workflow

1. Load Dataset
2. Data Cleaning
3. Data Preprocessing
4. Feature Selection
5. Train-Test Split
6. Model Training
7. Model Evaluation
8. Save Trained Model
9. Predict Student Performance

---

## ⚙ Installation

Clone the repository:

```bash
git clone https://github.com/your-username/upskillCampus.git
```

Move into the project directory:

```bash
cd upskillCampus
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## ▶ Running the Project

Train the model:

```bash
python code/train_model.py
```

Predict student performance:

```bash
python code/predict.py
```

Run the main application:

```bash
python code/main.py
```

---

## 📊 Expected Output

- Cleaned dataset
- Trained Machine Learning model
- Prediction results
- Accuracy score
- Confusion Matrix
- Classification Report
- Data Visualization Graphs

---

## 📷 Sample Output

```
Model Accuracy : 94.6%

Student Prediction

Study Hours : 6
Attendance : 90%
Previous Marks : 82

Predicted Result : PASS
```

---

## 📌 Future Enhancements

- Web-based dashboard using Flask or Django
- Integration with school databases
- Real-time student performance monitoring
- Deep Learning-based prediction model
- Automated report generation
- Email alerts for at-risk students

---

## 📖 Learning Outcomes

Through this project, the following skills are developed:

- Python Programming
- Data Analysis
- Data Preprocessing
- Machine Learning
- Model Evaluation
- Data Visualization
- GitHub Project Management
- Problem Solving

---

## 👨‍💻 Developed By

**Student Name:** *  BALAJISANKARAVEL A*

**Internship:** Winter Internship 2026

**Organization:** upskill Campus & UniConverge Technologies Pvt. Ltd.

---

## 📄 License

This project is developed for educational and internship purposes only.

---

## 🙏 Acknowledgement

I sincerely thank **upskill Campus**, **UniConverge Technologies Pvt. Ltd. (UCT)**, and my mentors for providing the opportunity, guidance, and resources to successfully complete this internship project. Their support and encouragement greatly contributed to the successful development of this machine learning application.
