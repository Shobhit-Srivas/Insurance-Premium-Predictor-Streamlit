# 💰 Insurance Premium Predictor

![Python](https://img.shields.io/badge/Python-3.12-blue?style=for-the-badge\&logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-App-red?style=for-the-badge\&logo=streamlit)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-ML-orange?style=for-the-badge\&logo=scikitlearn)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-purple?style=for-the-badge\&logo=pandas)

## 📌 Project Overview

The **Insurance Premium Predictor** is a Machine Learning web application developed using **Python**, **Scikit-Learn**, and **Streamlit** that predicts a user's estimated insurance premium based on demographic and health-related information.

The project demonstrates a complete Machine Learning workflow including:

* 📥 Data Collection
* 🧹 Data Preprocessing
* 📊 Exploratory Data Analysis (EDA)
* ⚙️ Feature Engineering
* 🤖 Model Training
* 📈 Model Evaluation
* 🌐 Streamlit Deployment

Users can enter personal information such as age, gender, BMI, smoking status, number of children, and region to receive an instant insurance premium prediction.

---

## 🎯 Objectives

* Predict medical insurance charges accurately.
* Perform detailed data analysis.
* Apply feature engineering techniques.
* Train and evaluate a regression model.
* Deploy the model using Streamlit.
* Build an end-to-end Data Science project.

---

## 📂 Project Structure

```text
Insurance-Premium-Predictor-Streamlit
│
├── app.py
├── train_model.py
├── insurance.csv
├── insurance_model.pkl
├── scaler.pkl
├── requirements.txt
│
├── pages
│   ├── 1_EDA.py
│   └── 2_Model_Performance.py
│
└── README.md
```

---

## 📊 Dataset Information

The dataset contains information about insurance beneficiaries.

### Features

| Feature  | Description            |
| -------- | ---------------------- |
| Age      | Age of the individual  |
| Sex      | Gender                 |
| BMI      | Body Mass Index        |
| Children | Number of dependents   |
| Smoker   | Smoking status         |
| Region   | Residential region     |
| Charges  | Insurance premium cost |

---

## 🔍 Exploratory Data Analysis

The project includes a dedicated EDA page built with Streamlit.

### Analysis Performed

✅ Dataset Overview

✅ Charges Distribution

✅ Age vs Insurance Charges

✅ Smoker Impact Analysis

✅ Feature Relationships

### Visualizations

* 📈 Histogram
* 📊 Scatter Plot
* 📉 Distribution Analysis

---

## ⚙️ Data Preprocessing

Several preprocessing techniques were applied:

### Encoding

* Male → 0

* Female → 1

* No Smoker → 0

* Smoker → 1

### Region Encoding

One-Hot Encoding was used for:

* Region Northwest
* Region Southeast
* Region Southwest

### Feature Engineering

Created:

```python
bmi_category_obese
```

This feature identifies whether BMI is greater than or equal to 30.

### Feature Scaling

StandardScaler was applied on:

* Age
* BMI
* Children

---

## 🤖 Machine Learning Model

### Algorithm Used

```text
Linear Regression
```

Linear Regression was selected to predict continuous insurance charge values.

### Workflow

1️⃣ Load Dataset

2️⃣ Clean Data

3️⃣ Encode Features

4️⃣ Scale Numerical Features

5️⃣ Train-Test Split

6️⃣ Train Linear Regression Model

7️⃣ Save Model using Joblib

---

## 🚀 Streamlit Application

The Streamlit application allows users to:

### Input Parameters

* Age
* Gender
* BMI
* Number of Children
* Smoking Status
* Region

### Output

💰 Predicted Insurance Premium

The prediction is generated instantly using the trained machine learning model.

---

## 🛠️ Technologies Used

### Programming Language

* Python 🐍

### Libraries

* Pandas
* NumPy
* Scikit-Learn
* Joblib
* Plotly
* Streamlit

---

## 📦 Installation

### Clone Repository

```bash
git clone https://github.com/Shobhit-Srivas/Insurance-Premium-Predictor-Streamlit.git
```

### Move into Project Folder

```bash
cd Insurance-Premium-Predictor-Streamlit
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run Model Training

```bash
python train_model.py
```

This generates:

```text
insurance_model.pkl
scaler.pkl
```

---

## ▶️ Run Streamlit App

```bash
streamlit run app.py
```

---

## 📸 Application Pages

### 🏠 Home Page

Insurance premium prediction form.

### 📊 EDA Page

Interactive visualizations and insights.

### 🤖 Model Performance Page

Displays machine learning model details and evaluation metrics.

---

## 📈 Future Improvements

* 🎨 Advanced UI Design
* 📄 PDF Report Generation
* ☁️ Cloud Deployment
* 📊 More Visualizations
* 🤖 Multiple ML Algorithms
* 🏆 Model Comparison Dashboard

---

## 🎓 Skills Demonstrated

* Data Cleaning
* Data Analysis
* Data Visualization
* Feature Engineering
* Machine Learning
* Model Deployment
* Streamlit Development
* Python Programming

---

## 👨‍💻 Author

### Shobhit Srivastava

Aspiring Data Analyst & Data Scientist passionate about Machine Learning, Data Analytics, Python, SQL, Power BI, and AI-driven solutions.

⭐ If you found this project useful, don't forget to star the repository!
