# Regex Pattern Examples

This directory demonstrates how to use AI models for generating and understanding regular expressions through practical examples in both JavaScript and Python. Each exercise includes clear input/output examples to help the AI model understand the requirements.

## Learning Objectives

- Learn how to use AI models to generate regex patterns
- Understand pattern requirements through clear input/output examples
- Practice writing and testing regular expressions
- Compare different AI models' approaches to regex generation

## Directory Structure

```
javascript/
  regex_helper.js  - JavaScript implementation of regex patterns
python/
  regex_helper.py  - Python implementation of regex patterns
```

## Exercise Format

Each exercise follows this format:

```python
# Exercise Name
# Input: "example input string"
# Output: ["expected", "output", "format"]
# Description: Detailed description of what the pattern should match
def function_name(input):
    pattern = r'regex_pattern_here'
    return result
```

## Included Exercises

1. Capital Letter Words

   ```python
   # Input: "Hello World Python Programming"
   # Output: ["Hello", "World", "Python", "Programming"]
   ```

2. Email Extraction

   ```python
   # Input: "Contact us at: support@example.com or sales.dept@company.co.uk"
   # Output: ["support@example.com", "sales.dept@company.co.uk"]
   ```

3. Date Format Validation

   ```python
   # Input: "2024-01-15" or "2024/01/15" or "15-01-2024"
   # Output: True/False
   ```

4. Phone Number Format

   ```python
   # Input: "+1-555-123-4567" or "(555) 123-4567"
   # Output: True/False
   ```

5. URL Components

   ```python
   # Input: "https://api.example.com/v1/users?id=123#profile"
   # Output: {
   #     "protocol": "https",
   #     "domain": "api.example.com",
   #     "path": "/v1/users",
   #     "query": "id=123",
   #     "fragment": "profile"
   # }
   ```

6. Password Strength

   ```python
   # Input: "MyP@ssw0rd123"
   # Output: True/False
   ```

7. Code Comment Extraction

   ```python
   # Input: "def hello(): # Say hello\\n    print('Hello') # Print greeting"
   # Output: ["Say hello", "Print greeting"]
   ```

8. Version Number Parsing

   ```python
   # Input: "v1.2.3-alpha.1"
   # Output: {
   #     "major": "1",
   #     "minor": "2",
   #     "patch": "3",
   #     "label": "alpha.1"
   # }
   ```

9. HTML Tag Extraction

   ```python
   # Input: "<div class='container'><p>Hello</p></div>"
   # Output: ["div", "p"]
   ```

10. Log Entry Parsing
    ```python
    # Input: "2024-01-15 10:30:45 [ERROR] Failed to connect: timeout"
    # Output: {
    #     "date": "2024-01-15",
    #     "time": "10:30:45",
    #     "level": "ERROR",
    #     "message": "Failed to connect: timeout"
    # }
    ```

## Comparing AI Models

When evaluating different AI models on these exercises, observe:

1. Pattern Accuracy

   - Correctness of the generated pattern
   - Handling of edge cases
   - Proper use of regex features

2. Code Quality

   - Pattern readability
   - Use of named groups
   - Error handling
   - Performance considerations

3. Understanding

   - Interpretation of requirements
   - Recognition of input/output format
   - Handling of multiple formats

4. Documentation
   - Pattern explanation
   - Usage examples
   - Edge case documentation

## Testing the Patterns

Each exercise includes:

- Multiple test cases
- Edge case examples
- Invalid input handling
- Performance considerations

## Best Practices

1. Clear Input/Output Examples

   - Show exact input format
   - Demonstrate expected output
   - Include edge cases

2. Pattern Documentation

   - Explain pattern components
   - Document limitations
   - Note performance implications

3. Error Handling
   - Handle invalid inputs
   - Provide meaningful errors
   - Consider edge cases
