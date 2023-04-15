# -*- coding: utf-8 -*-
"""customer_churn_prediction

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1kmIn4c6WiWWEkJM5tisAMywbiAIe9iJw
"""

from IPython.display import Image
Image(url='https://www.revechat.com/wp-content/uploads/2015/08/leaving-website.jpg')

# Importing the essential Libraries
import pandas as pd
import numpy as np
import seaborn as sns

# Reading the Dataset
df = pd.read_csv('/content/Churn_Modelling.csv')

df.head()

df.shape

df.columns

df.dtypes

# Printing Unique Values of the categorical variables
print(df['Geography'].unique())
print(df['Gender'].unique())
print(df['NumOfProducts'].unique())
print(df['HasCrCard'].unique())
print(df['IsActiveMember'].unique())

# Checking if there are null values or not
df.isna().sum()

df.describe()

df.head()

# Including only Potential Predictors as independent varibles
final_dataset = df[['CreditScore', 'Geography', 'Gender', 'Age', 'Tenure', 'Balance', 'NumOfProducts', 'HasCrCard', 'IsActiveMember', 'EstimatedSalary', 'Exited']]

final_dataset.head()

# Converting the categorical variables into numerical and avoiding Dummy Varibale Trap
final_dataset = pd.get_dummies(final_dataset, drop_first=True)

final_dataset.head()

sns.pairplot(final_dataset)

# Splitting the Dataset into Dependent and Independent Variables
X = final_dataset.iloc[:, [0,1,2,3,4,5,6,7,9,10,11]]
y = final_dataset.iloc[:, 8].values

X.head()

y

# Splitting the dataset into Training and Testing Data
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2, random_state = 42)

# Standardizing the Dataset
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

print(X_train)

## Feature Importance
from sklearn.ensemble import ExtraTreesRegressor
model = ExtraTreesRegressor()
model.fit(X,y)

print(model.feature_importances_)

from sklearn.ensemble import RandomForestClassifier
rf = RandomForestClassifier()
rf.fit(X_train,y_train)

y_pred = rf.predict(X_test)

#confusion matrix to visualize and summarize the classification algorithm
from sklearn.metrics import accuracy_score, confusion_matrix
cm = confusion_matrix(y_test,y_pred)
print(cm)
print(accuracy_score(y_test,y_pred))

# pickling the Model
import pickle
file = open('Customer_Churn_Prediction.pkl', 'wb')
pickle.dump(rf, file)