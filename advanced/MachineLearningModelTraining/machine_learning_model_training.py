# This is a Python script to demonstrate training a machine learning model using GitHub Copilot.

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Function to preprocess the data
def preprocess_data(file_path):
    # Load the data into a DataFrame
    data = pd.read_csv(file_path)
    # Split the data into features and target
    X = data.drop("target", axis=1)
    y = data["target"]
    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    # Standardize the features
    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)
    # Return the preprocessed data
    return X_train, X_test, y_train, y_test

# Function to train the model
def train_model(X_train, y_train):
    # Create a logistic regression model
    model = LogisticRegression()
    # Train the model
    model.fit(X_train, y_train)
    # Return the trained model
    return model

# Function to evaluate the model
def evaluate_model(model, X_test, y_test):
    # Make predictions
    y_pred = model.predict(X_test)
    # Calculate the accuracy
    accuracy = accuracy_score(y_test, y_pred)
    # Return the accuracy
    return accuracy

# Example usage
file_path = "data.csv"
X_train, X_test, y_train, y_test = preprocess_data(file_path)
model = train_model(X_train, y_train)
accuracy = evaluate_model(model, X_test, y_test)
print(f"Model accuracy: {accuracy}")
