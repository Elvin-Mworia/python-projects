import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split, cross_val_score, learning_curve
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import math
import warnings

# Load your historical stock price data into a DataFrame
data = pd.read_csv('COOP.csv')
print(type(data))

data['Date']=pd.to_datetime(data['Date'])
data=data.sort_values(by='Date', ascending=True)

# Preprocess the 'Date' column into numerical features
data['Day'] = pd.to_datetime(data['Date'], format='%d-%b-%y').dt.day
data['Month'] = pd.to_datetime(data['Date'], format='%d-%b-%y').dt.month
data['Year'] = pd.to_datetime(data['Date'], format='%d-%b-%y').dt.year

# Extract the features and target variable
X = data[['Previous','Day High','Day Low','Volume']]
y = data['Day Price']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create a Linear Regression model
model = LinearRegression()

# Fit the model on the training data
model.fit(X_train, y_train)

# Perform k-fold cross-validation
cv_scores = cross_val_score(model, X, y, scoring='neg_mean_squared_error', cv=5)
print("Cross-Validation Scores (Negative MSE):", -cv_scores)
print("Average Cross-Validation Score:", -cv_scores.mean())


# Make predictions on the test data
y_pred = model.predict(X_test)

# Calculate RMSE (Root Mean Squared Error)
rmse = math.sqrt(mean_squared_error(y_test, y_pred))
print(f"RMSE: {rmse}")

# R-squared (coefficient of determination) score
r2 = r2_score(y_test, y_pred)
print(f"R-squared score: {r2:.2f}")

# Generate learning curves
def plot_learning_curve(model, X, y):
    train_sizes, train_scores, test_scores = learning_curve(model, X, y, cv=5, scoring='neg_mean_squared_error')
    
    train_scores_mean = -np.mean(train_scores, axis=1)
    train_scores_std = np.std(train_scores, axis=1)
    test_scores_mean = -np.mean(test_scores, axis=1)
    test_scores_std = np.std(test_scores, axis=1)
    
    plt.figure(figsize=(10, 6))
    plt.title("Learning Curves")
    plt.xlabel("Training Examples")
    plt.ylabel("Negative MSE")
    
    plt.fill_between(train_sizes, train_scores_mean - train_scores_std, train_scores_mean + train_scores_std, alpha=0.1, color="r")
    plt.fill_between(train_sizes, test_scores_mean - test_scores_std, test_scores_mean + test_scores_std, alpha=0.1, color="g")
    
    plt.plot(train_sizes, train_scores_mean, 'o-', color="r", label="Training Score")
    plt.plot(train_sizes, test_scores_mean, 'o-', color="g", label="Cross-Validation Score")
    
    plt.legend(loc="best")
    plt.grid()
    plt.show()

# Plot Learning Curves
plot_learning_curve(model, X, y)

#Plotting the actual vs predicted values
data = data.sort_values(by='Date')
plt.figure(figsize=(12, 6))
plt.plot(y_test.values, label='Actual Prices', marker='o', linestyle='-')
plt.plot(y_pred, label='Predicted Prices', marker='o', linestyle='--')
plt.title('Actual vs. Predicted Prices')
plt.xlabel('Test Data')
plt.ylabel('Day Price/Close Price')
plt.legend()
plt.grid()
plt.show()

with warnings.catch_warnings():
    warnings.simplefilter("ignore", category=UserWarning)




