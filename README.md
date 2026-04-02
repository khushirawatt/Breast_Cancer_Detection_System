 Breast Cancer Detection System using Machine Learning
 
 
** Overview **

Breast cancer is one of the most common and life-threatening diseases. Early detection can significantly improve survival rates.
This project presents a Machine Learning-based system that predicts whether a tumor is Malignant (Cancerous) or Benign (Non-Cancerous) using medical data.

 ** Problem Statement **

Early diagnosis of breast cancer is difficult and requires expert medical analysis. Manual diagnosis can be time-consuming and prone to error.

 ** Solution **

This system uses Logistic Regression, a supervised machine learning algorithm, to analyze tumor characteristics and predict cancer presence quickly and accurately.

** 📊 Dataset Information **
Total Records: 569 patients
Total Features: 33 columns
Target Variable: Diagnosis (M = Malignant, B = Benign)

The dataset includes features such as:

Radius, Texture, Perimeter, Area
Smoothness, Compactness, Concavity
Symmetry and Fractal Dimension

These features are derived from digitized images of breast masses.

** Tech Stack **
Frontend: HTML, CSS
Backend: Flask (Python)
Machine Learning: Scikit-learn
Data Handling: Pandas, NumPy

** How It Works **
User inputs tumor-related data through the interface
Data is sent to the backend using Flask
The trained Logistic Regression model processes the data
The system predicts:
Malignant (Cancer)
Benign (No Cancer)
Result is displayed to the user

** Features **
Simple and user-friendly interface
Fast and accurate predictions
Real-time result display
Lightweight and efficient ML model

** Model Used **
Logistic Regression
Suitable for binary classification
Provides probability-based predictions
Efficient for small and structured datasets
