
# Exercise: String Formatter
# Practice string manipulation tasks with Github Copilot

sample_text = "Hello, World! This is a TEST string 123"

# TODO: Write a function that converts the string to alternate upper and lower case
def alternate_case(text):
    result = ""
    for i, char in enumerate(text):
        if i % 2 == 0:
            result += char.upper()
        else:
            result += char.lower()
    return result

# TODO: Write a function that counts vowels and consonants
def count_vowels_consonants(text):
    vowels = "aeiouAEIOU"
    num_vowels = 0
    num_consonants = 0
    for char in text:
        if char.isalpha():
            if char in vowels:
                num_vowels += 1
            else:
                num_consonants += 1
    return num_vowels, num_consonants

# TODO: Write a function that extracts all numbers from the string
def extract_numbers(text):
    return [int(char) for char in text if char.isdigit()]