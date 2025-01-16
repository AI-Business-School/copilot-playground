# This is a simple Python script to demonstrate converting JSON to a User class and vice versa using GitHub Copilot.

import json

# Define a User class
class User:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

# Create a JSON representation of a user
user_json = {
    "name": "John Doe",
    "email": "johndoe@gmail.com",
    "password": "password123"
}

# Function to serialize JSON to User class
def create_user(json_data):
    # Parse the JSON data
    data = json.loads(json_data)
    # Create a User object
    user = User(data['name'], data['email'], data['password'])
    return user

# Function to deserialize User class to JSON
def jsonify_user(user):
    # Create a dictionary from the User object
    user_dict = {
        "name": user.name,
        "email": user.email,
        "password": user.password
    }
    # Convert the dictionary to JSON
    return json.dumps(user_dict)

# Example usage
user_instance = create_user(json.dumps(user_json))
print(f"User name: {user_instance.name}, User email: {user_instance.email}")

user_json_str = jsonify_user(user_instance)
print(f"User JSON: {user_json_str}")
