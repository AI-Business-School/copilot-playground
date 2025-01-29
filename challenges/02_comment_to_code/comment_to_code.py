# Example 1: Simple function with array input
# Function name: calculate_average
# Input: numbers (list of numbers)
# Output: float (average of the list)
def calculate_average(numbers):
    return sum(numbers) / len(numbers)

# Example 2: String manipulation
# Function name: reverse_and_capitalize
# Input: text (string)
# Output: reversed and capitalized string
def reverse_and_capitalize(text):
    return text[::-1].upper()

# Example 3: Dictionary transformation
# Function name: format_person
# Input: person (dict with name and age)
# Output: formatted string
def format_person(person):
    return f"{person['name']} is {person['age']} years old"
