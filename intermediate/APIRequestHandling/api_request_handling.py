# This is a Python script to demonstrate handling API requests using GitHub Copilot.

import requests

# Function to send a GET request
def send_get_request(url):
    # Send the GET request
    response = requests.get(url)
    # Check if the request was successful
    if response.status_code == 200:
        # Return the response content
        return response.content
    else:
        # Return an error message
        return f"Error: {response.status_code}"

# Function to send a POST request
def send_post_request(url, data):
    # Send the POST request
    response = requests.post(url, json=data)
    # Check if the request was successful
    if response.status_code == 200:
        # Return the response content
        return response.content
    else:
        # Return an error message
        return f"Error: {response.status_code}"

# Example usage
get_url = "https://jsonplaceholder.typicode.com/posts/1"
post_url = "https://jsonplaceholder.typicode.com/posts"
post_data = {
    "title": "foo",
    "body": "bar",
    "userId": 1
}

# Send a GET request
get_response = send_get_request(get_url)
print(f"GET response: {get_response}")

# Send a POST request
post_response = send_post_request(post_url, post_data)
print(f"POST response: {post_response}")
