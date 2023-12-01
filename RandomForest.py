import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix, auc, roc_curve,accuracy_score
import matplotlib.pyplot as plt
import seaborn as sns

# Load your historical stock price data into a DataFrame
data = pd.read_csv('clean_data.csv')

# Preprocess the 'Date' column into numerical features
data['Day'] = pd.to_datetime(data['Date'], format='%d-%b-%y').dt.day
data['Month'] = pd.to_datetime(data['Date'], format='%d-%b-%y').dt.month
data['Year'] = pd.to_datetime(data['Date'], format='%d-%b-%y').dt.year

# target variable (for example, 'BuyOrSell') indicating whether to buy or sell
data['BuyOrSell'] = pd.DataFrame(np.where(data['Previous'].shift(-1) > data['Previous'], 1, 0))

# Extract the features and target variable
X = data[['Previous','Day High','Day Low','Day Price','Volume']]
y = data['BuyOrSell']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=44)

# Create a Random Forest Classifier
rf_classifier = RandomForestClassifier(n_estimators=100, random_state=44)

# Train the model
rf_classifier.fit(X_train, y_train)

# Make predictions on the test data
y_pred = rf_classifier.predict(X_test)

# Confusion Matrix
conf_matrix = confusion_matrix(y_test, y_pred)

# Plot Confusion Matrix as Heatmap
plt.figure(figsize=(8, 6))
sns.heatmap(conf_matrix, annot=True, fmt='d', cmap='Blues', cbar=False)
plt.title('Confusion Matrix')
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.show()

# Accuracy Score
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy Score:", accuracy)

# ROC Curve and AUC
y_prob = rf_classifier.predict_proba(X_test)[:, 1]
fpr, tpr, _ = roc_curve(y_test, y_prob)
roc_auc = auc(fpr, tpr)

# Plot ROC Curve
plt.figure(figsize=(8, 6))
plt.plot(fpr, tpr, color='darkorange', lw=2, label='ROC curve (AUC = {:.2f})'.format(roc_auc))
plt.plot([0, 1], [0, 1], color='navy', lw=2, linestyle='--')
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('Receiver Operating Characteristic (ROC) Curve')
plt.legend()
plt.show()

# Area under the ROC curve (AUC)
print("AUC:", roc_auc)