# -*- coding: utf-8 -*-
"""HomeValue Predictor: A Linear Regression Approach01.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1PLuDenNcKIpSH4Q2-qWKknNwfe0QlB9f
"""

# Importing Required Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

# 1. Data Loading

# Load the dataset (Make sure the path to your dataset is correct)
df = pd.read_csv("/content/Housing.csv")

# Display first 5 rows to understand the data structure
print(df.head())

# Get a summary of the dataset

df.describe()

# Check for missing values

print(df.isnull().sum())

# 2. Data Preprocessing

# Encoding categorical variables to numeric values
categorical_features = ['furnishingstatus', 'prefarea', 'airconditioning',
                        'hotwaterheating', 'basement', 'guestroom', 'mainroad']

le = LabelEncoder()
for feature in categorical_features:
    df[feature] = le.fit_transform(df[feature])

# 3. Exploratory Data Analysis (EDA)

# Correlation heatmap to see relationships between features
plt.figure(figsize=(10,8))
sns.heatmap(df.corr(), annot=True, cmap="coolwarm")
plt.title("Feature Correlation Heatmap")
plt.show()

# Distribution of house prices
plt.figure(figsize=(8,5))
sns.histplot(df['price'], kde=True, color='skyblue')
plt.title("Distribution of House Prices")
plt.xlabel("Price")
plt.ylabel("Frequency")
plt.show()

# Features and target variable
X = df.drop('price', axis=1)  # Features
y = df['price']              # Target

# 4. Train-Test Split

# Split data into training and testing sets (80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 5. Model Training

# Initialize and train the Linear Regression model
model = LinearRegression()
model.fit(X_train, y_train)

# 6. Model Evaluation

# Predict house prices on the test set
y_pred = model.predict(X_test)

# Evaluation Metrics
mse = mean_squared_error(y_test, y_pred)
mae = mean_absolute_error(y_test, y_pred)
rmse = np.sqrt(mse)
r_squared = r2_score(y_test, y_pred)

# Display evaluation metrics
print("\nModel Performance:")
print(f"Mean Absolute Error (MAE): {mae:.2f}")
print(f"Mean Squared Error (MSE): {mse:.2f}")
print(f"Root Mean Squared Error (RMSE): {rmse:.2f}")
print(f"R-squared (R²): {r_squared:.2f}")

# 7. Visualization of Results

# Actual vs Predicted Plot
plt.figure(figsize=(8,5))
plt.scatter(y_test, y_pred, color='red', edgecolor='k', alpha=0.7)
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], color='blue', linestyle='--', linewidth=2)
plt.xlabel("Actual Prices")
plt.ylabel("Predicted Prices")
plt.title("Actual vs Predicted House Prices")
plt.grid(True, linestyle='--', alpha=0.6)
plt.show()

# Residuals Plot (to check for patterns and heteroscedasticity)
residuals = y_test - y_pred
plt.figure(figsize=(8,5))
plt.scatter(y_pred, residuals, color='purple', edgecolor='k', alpha=0.7)
plt.axhline(0, color='black', linestyle='--', linewidth=1.5)
plt.xlabel("Predicted Prices")
plt.ylabel("Residuals")
plt.title("Residuals vs Predicted Prices")
plt.grid(True, linestyle='--', alpha=0.6)
plt.show()

# 8. Conclusion

"""
This script provides a comprehensive linear regression approach to predict house prices.
It includes thorough data exploration, preprocessing, model training, and detailed evaluation
with visualizations. The improved comments and code readability make it suitable for showcasing.
"""