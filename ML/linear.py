import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

# Step 1: Load the Iris dataset
iris = load_iris()
X = iris.data  # Features: sepal length, sepal width, petal length, petal width
y = iris.target  # Target: species of the flower (not used in regression)

# For this example, we will predict 'petal length' using other features (sepal length, sepal width, petal width)
# We use petal length (index 2) as the target variable for regression.
y = X[:, 2]  # Petal length is the third feature in the dataset

# Step 2: Split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Step 3: Create a linear regression model
model = LinearRegression()

# Step 4: Train the model using the training data
model.fit(X_train, y_train)

# Step 5: Make predictions using the test data
y_pred = model.predict(X_test)

# Step 6: Evaluate the model
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

# Step 7: Print the results
print(f"Mean Squared Error (MSE): {mse}")
print(f"R-squared (R2): {r2}")
print(f"Model Coefficients: {model.coef_}")
print(f"Intercept: {model.intercept_}")

# Step 8: Plot Actual vs Predicted values
plt.figure(figsize=(8, 6))
plt.scatter(y_test, y_pred, color='blue')
plt.plot([min(y_test), max(y_test)], [min(y_test), max(y_test)], color='red', linewidth=2)  # Line of perfect prediction
plt.title('Actual vs Predicted Petal Length')
plt.xlabel('Actual Petal Length')
plt.ylabel('Predicted Petal Length')
plt.show()

# Step 9: Plot Petal Width vs Petal Length
plt.figure(figsize=(8, 6))
plt.scatter(X[:, 3], y, color='green')  # X[:, 3] is petal width
plt.title('Petal Width vs Petal Length')
plt.xlabel('Petal Width')
plt.ylabel('Petal Length')
plt.show()
