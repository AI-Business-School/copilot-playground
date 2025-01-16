# This is a Python script to demonstrate data analysis with Pandas using GitHub Copilot.

import pandas as pd
import matplotlib.pyplot as plt

# Function to load data from a CSV file
def load_data(file_path):
    # Load the data into a DataFrame
    data = pd.read_csv(file_path)
    # Return the DataFrame
    return data

# Function to analyze the data
def analyze_data(data):
    # Print the first 5 rows of the DataFrame
    print("First 5 rows of the data:")
    print(data.head())
    # Print the summary statistics of the DataFrame
    print("\nSummary statistics of the data:")
    print(data.describe())

# Function to visualize the data
def visualize_data(data, column):
    # Plot the data
    plt.figure(figsize=(10, 6))
    plt.plot(data[column])
    plt.title(f"{column} over Time")
    plt.xlabel("Time")
    plt.ylabel(column)
    plt.show()

# Example usage
file_path = "data.csv"
data = load_data(file_path)
analyze_data(data)
visualize_data(data, "column_name")
