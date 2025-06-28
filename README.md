# Diabetes_prediction
This repository contains a simple Diabetes Prediction web application built with Streamlit. The app predicts whether a patient is likely to have diabetes using a trained machine learning model.🩺 Diabetes Prediction App with Streamlit
This repository contains a simple Diabetes Prediction web application built with Streamlit. The app predicts whether a patient is likely to have diabetes using a trained machine learning model.

# Project Files
File/Folder   Purpose

diabetes.csv = Dataset used to train the model (Pima Indians Diabetes Database)

diabetes.pkl	=Saved trained machine learning model

myapp.py = Streamlit app script

notebook.ipynb	= Jupyter notebook for EDA and model building

photos      =	Contains screenshots of the app and its title page

# How It Works
User Input: The app takes medical input values such as pregnancies, glucose level, blood pressure, BMI, etc.

Prediction: The trained model (diabetes.pkl) predicts whether the patient is likely to have diabetes.

Output: Displays the prediction result directly in the app.

# How to Run This App Locally
1️⃣ Clone the Repository
bash
Copy
Edit
git clone https://github.com/your-username/diabetes-prediction-app.git
cd diabetes-prediction-app
2️⃣ Install Dependencies
Create a virtual environment (optional but recommended):

bash
Copy
Edit
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
Install required packages:

bash
Copy
Edit
pip install -r requirements.txt

3️⃣ Run the Streamlit App
bash
Copy
Edit
streamlit run myapp.py
Open the link provided by Streamlit in your browser (e.g., http://localhost:8501).

# Screenshots

App Title Page 

Working App

Prediction Result

# Model Performance
Algorithm: XGBClassifier

Accuracy: Training: 93% , Testing: 80%

Metrics: Confusion matrix

# Requirements
Python 3

pandas

numpy

scikit-learn

streamlit

PIL

# Dataset
Source: Pima Indians Diabetes Database
