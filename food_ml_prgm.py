# -*- coding: utf-8 -*-
"""food ml prgm

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1aq-ZWUdGFUBO26oyFObvmPWdgsJ8aHz2
"""

import pandas as pd

# Load data from the CSV file
data = pd.read_csv('/content/food.csv')

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.pipeline import make_pipeline
from sklearn.svm import LinearSVC
from sklearn.metrics import accuracy_score

# Load data from the CSV file
data = pd.read_csv('/content/food.csv')

# Preprocess the data
# Adjust column names according to your dataset
X = data['Description'].fillna('').astype(str)
y = data['Data.Alpha Carotene']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create a pipeline for text classification
model = make_pipeline(
    TfidfVectorizer(),
    LinearSVC()
)

# Train the model
model.fit(X_train, y_train)

# Evaluate the model
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.pipeline import make_pipeline
from sklearn.svm import LinearSVC
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# Load data from the CSV file
data = pd.read_csv('/content/food.csv')

# Preprocess the data
# Adjust column names according to your dataset
X = data['Description'].fillna('').astype(str)
y = data['Data.Alpha Carotene']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create a pipeline for text classification
model = make_pipeline(
    TfidfVectorizer(),
    LinearSVC()
)

# Train the model
model.fit(X_train, y_train)

# Evaluate the model
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)

# Additional Evaluation Metrics
print("\nClassification Report:")
print(classification_report(y_test, y_pred))

print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))

# Error Analysis
errors = X_test[y_test != y_pred]
error_labels = y_test[y_test != y_pred]
error_predictions = y_pred[y_test != y_pred]
error_analysis = pd.DataFrame({'Text': errors, 'True Label': error_labels, 'Predicted Label': error_predictions})
print("\nError Analysis:")
print(error_analysis.head())

# Deploy the Model
# You can deploy the model using frameworks like Flask, FastAPI, or as part of a cloud service like AWS Lambda or Google Cloud Functions
# Here's a simple example using Flask:
# from flask import Flask, request, jsonify
# app = Flask(__name__)
# @app.route('/predict', methods=['POST'])
# def predict():
#     data = request.get_json(force=True)
#     prediction = model.predict([data['text']])[0]
#     return jsonify({'prediction': prediction})
# if __name__ == '__main__':
#     app.run(debug=True)

pip install flask

from flask import Flask, request, jsonify
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.pipeline import make_pipeline
from sklearn.svm import LinearSVC

# Load data from the CSV file
data = pd.read_csv('/content/food.csv')

# Preprocess the data
X = data['Description'].fillna('').astype(str)
y = data['Data.Alpha Carotene']

# Create a pipeline for text classification
model = make_pipeline(
    TfidfVectorizer(),
    LinearSVC()
)

# Train the model
model.fit(X, y)

# Create Flask app
app = Flask(__name__)

# Define prediction route
@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json(force=True)
    text = data['text']
    prediction = model.predict([text])[0]
    return jsonify({'prediction': prediction})

if __name__ == '__main__':
    app.run(debug=True)