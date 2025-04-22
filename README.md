# 📊 Telecom Customer Churn Analysis

In today’s highly competitive telecom market, retaining existing customers is more crucial than ever. Customer churn when users switch to a different provider can have a major impact on a company’s revenue and growth. This project aims to develop a predictive model that identifies customers who are at risk of leaving, based on their behavior, service usage, and demographic patterns. By uncovering these insights, telecom companies can take proactive steps to improve satisfaction and reduce churn.

This repository contains all the resources needed for churn analysis, including the dataset, data preprocessing, modeling code, and results. It also highlights key factors influencing churn and provides actionable strategies to enhance customer retention and loyalty.

---

## Table of Contents
- [Problem Statement](#problem-statement)
- [Objectives](#Objectives)
- [Data Collection & Preparation](#Data-Collection-and-Preparation)
- [Exploratory Data Analysis (EDA)](#Exploratory-Data-Analysis-(EDA))
- [Modeling](#Modeling)
- [Dashboard](#Dashboard)
- [Key Insights](#Key-Insights)
- [Recommendations](#Recommendations)
- [Tools & Technologies Used](#Tools-and-Technologies-Used)
- [Conclusion](#Conclusion)
- [References](#references)
- [Project Setup](#Project-Setup)
---

## Problem Statement

Telecom companies have high churn among their users, a direct impact on revenue. The data of the customers must be examined to identify the most significant churn metrics and develop a predictive model to classify the high-risk customers. Business purposes are to enable enterprises to take proactive retention measures and improve customer satisfaction.

--- 

## Objectives

- Understand patterns behind customer churn.
- Identify the most influential factors contributing to churn.
- Build machine learning models to predict churn.
- Visualize churn trends through dashboards.
- Provide recommendations for improving customer retention.

---

## Data Collection and Preparation

- Dataset Source: Kaggle - Telco Customer Churn

- Cleaning:
    - Removed missing or inconsistent values.
    - Converted categorical variables using label encoding and one-hot encoding.
    - Created new features such as `ServicesCount`,`PaymentMethodType`, `ChargeRatio`, and `HighRisk`.
    - Remove Outliers using IQR method.
    - Handled imbalanced data using SMOTE for oversampling.

---

## Exploratory Data Analysis (EDA)

- Conducted in-depth EDA to uncover hidden patterns, correlations, and anomalies within the dataset.
- Visualize numerical and categorical features seperately using different kind of graphs like Bar, pie and histogram.
- Explore the relationship between numerical and categorical features with target variable (Churn)

--- 

## Modeling

Used multiple classification models to predict churn:
- Decision Tree
- Random Forest
- XGBoost Classifier
- Balanced Bagging Classifier

## Model Evaluation:

Focused on Recall to minimize false negatives (i.e., predicting a churning customer as non-churn).
Evaluated using:
- Confusion Matrix
- F1 Score
- Precision & Recall
- ROC-AUC

---

## Dashboard

The project includes two separate dashboards:

| Demographics Dashboard | Services & Billing Dashboard |
|---------------|-------------|
| ![Demographics Dashboard]() | ![Services & Billing Dashboard]() |
| Highlights churn behavior based on gender, seniority, and age groups. | Focuses on service usage, billing type, internet service, and customer support. |

---

## Key Insights

- **Tenure matters:** New customers (less than 1 year) churn at much higher rates than long-term ones.
- **Contract type:** Month-to-month contracts see the highest churn.
- **Services count:** Fewer services used → higher churn risk; 4–5 services users are more stable.
- **Family status:** Customers with partners and dependents are less likely to churn.
- **Internet type:** Fiber optic users churn more than DSL or non-internet users.
- **Payment method:** Electronic check users face the highest churn and pay more on average.
- **Paperless billing:** Customers not using paperless billing churn less.

---

## Recommendations

- **Retain new customers** with welcome bonuses, loyalty points, and personalized plans.
- **Encourage bundling** and offer discounts for multi-service usage.
- **Promote long-term contracts** with exclusive deals.
- **Improve payment experience**, especially for electronic check users.
- **Cross-sell internet services** and monitor fiber optic user satisfaction.
- **Offer billing support** and collect feedback to resolve service or pricing concerns.
- **Launch referral programs** targeting customers with partners or dependents.

---

## Tools and Technologies Used

- **Python** (Pandas, Scikit-learn, XGBoost, Matplotlib, Seaborn)
- **Power BI** for dashboard creation
- **Jupyter Notebook** for model development
- **SMOTE** for handling class imbalance

--- 

## Conclusion
This churn analysis project helps telecom companies identify key churn signals early and take data-driven actions to retain at-risk customers. The dashboard provides a visual snapshot of the problem, while the machine learning model enables future churn prediction.

---

## References

- Kaggle. (n.d.). Telco Customer Churn Dataset. Retrieved from
https://www.kaggle.com/datasets/blastchar/telco-customer-churn

- imbalanced-learn. (n.d.). SMOTE Oversampling – imbalanced-learn Documentation. Retrieved from
https://imbalanced-learn.org/stable/references/generated/imblearn.over_sampling.SMOTE.html

- Scikit-learn. (n.d.). Machine Learning in Python. Retrieved from
https://scikit-learn.org/stable/

- Harvard Business Review. (2010). Stop Trying to Delight Your Customers. Retrieved from
https://hbr.org/2010/07/stop-trying-to-delight-your-customers

---

## Project Setup

### 🔁 Clone the Repository
```
git clone https://github.com/yourusername/telecom-churn-analysis.git
cd telecom-churn-analysis
```
### 📦 Install Dependencies
Make sure you’re in your virtual environment, then run:
```
pip install -r requirements.txt
```

---

## 📁 Project Structure
```
TELECOM-CHURN-ANALYSIS/
│
├── .venv/                          # Virtual environment folder
│
├── dashboard/                      # Dashboards and Tableau assets
│
├── data/                           # Raw and processed datasets
│
├── frontend/                       # Web application (Flask-based)
│   ├── model/                      # Trained models or pipeline files
│   ├── static/                     # Static assets (CSS, JS, images)
│   ├── templates/                 # HTML templates for the UI
│   └── app.py                      # Flask app to run the project
│
├── notebooks/                      # Jupyter notebooks for analysis
│   ├── data_cleaning.ipynb         # Data cleaning steps
│   ├── eda.ipynb                   # Exploratory Data Analysis
│   └── Modeling.ipynb              # Model training and evaluation
│
├── churn-img.png                   # Infographic/visual used in README
├── requirements.txt                # Python dependencies
├── Telecom Customer Churn Analysis Report.pdf  # Final project report
└── README.md                       # Project overview and documentation
```
---

## ▶️ Running the Project

- **Start the Application:** Execute the following command to run the project.

   ```bash
   python app.py
   ```

**After you have successfully installed and launched the project, you can utilize it to forecast customer churn. Follow these steps to begin:**

- **Access the Web Interface:** Open your web browser and navigate to:

   ```
   http://127.0.0.1:5000/
   ```

---

## 📜 License
This project is licensed under the MIT License – feel free to use, modify, and distribute with attribution.

---

## 🙌 Acknowledgments
- **Dataset**: [Telco Customer Churn Dataset](https://www.kaggle.com/datasets/blastchar/telco-customer-churn) from Kaggle
- **Inspiration**: Real-world telecom customer retention challenges
- **References**: Concepts inspired by case studies and research in customer behavior, churn prediction, and business analytics