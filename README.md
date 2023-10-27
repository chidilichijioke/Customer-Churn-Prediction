# Customer-Churn-Prediction

## EXECUTIVE SUMMARY
Customer churn refers to the loss of customers or subscribers for any reason at all. Businesses measure and track churn as a percentage of lost customers compared to the total number of customers over a given time period. This project aims to predict customer churn in a telecommunication business company, by employing machine learning techniques, using data containing customers information and churn status. This project also explores the building of a machine learning web application using the Streamlit framework.
## NTRODUCTION
Customer churn is the percentage of customers who stopped purchasing your business’s products or services during a certain period of time. Your customer churn rate indicates how many of your existing customers are not likely to make another purchase from your business. A high churn rate indicates that your customers are not satisfied with the products or services you’re offering.

The objective of this project are as follows:
* Explore and analyze dataset to gain insights into factors influencing churn
* Build a machine learning model to identify potential customer churn.
* Build a machine learning web application and deploy a model created to
identify churn.
 
This project focuses on predicting customer churn using historical customer data.
## METHODOLOGY
### DATA COLLECTION AND PREPROCESSING
The dataset used in this project was obtained from the IBM sample data. It contains information about customers churn status, services that each customer signed up for, customer account information and demographic information.
The dataset underwent cleaning to remove missing values, irrelevant columns were dropped and categorical columns one-hot encoded.
### FEATURE ENGINEERING
Features such as ‘Tenure’ were selected and transformed into a bin of 12 months to create a new feature ‘Tenure_grp’.
### EXPLORATORY DATA ANALYSIS (EDA)
EDA was performed to understand and gain insights from the data set.
#### DESCRIPTIVE STATISTICS


#### UNIVARIATE ANALYSIS
  2

 BIVARIATE ANALYSIS
  3

 CORRELATION ANALYSIS
  4

 MODEL BUILDING AND EVALUATION
MODEL TRAINING
Dataset was balanced using the SMOTEENN technique. The dataset was split into predictive features and target features and further splitted into training set and testing set to train and evaluate the model’s performance. Hyperparameter tuning was performed to optimize model accuracy.
   5

PREDICTIVE ANALYSIS
 6
The Decision Tree Classifier model had an accuracy of 94.04%
