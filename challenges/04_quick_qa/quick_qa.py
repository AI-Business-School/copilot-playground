# Example 1: Code Explanation Question
def process_data(items: list) -> dict:
    """
    Q: What does this function do? How can it be improved?
    """
    result = {}
    for item in items:
        if item in result:
            result[item] += 1
        else:
            result[item] = 1
    return result

# Example 2: Debugging Question
def calculate_average(numbers: list) -> float:
    """
    Q: Why might this function fail? What are the edge cases?
    """
    total = sum(numbers)
    return total / len(numbers)

# Example 3: Performance Question
def find_duplicates(array: list) -> list:
    """
    Q: How can we optimize this function for better performance?
    """
    duplicates = []
    for i in range(len(array)):
        for j in range(i + 1, len(array)):
            if array[i] == array[j] and array[i] not in duplicates:
                duplicates.append(array[i])
    return duplicates

# Example 4: Best Practices Question
class DataProcessor:
    """
    Q: How can we improve this class following Python best practices?
    """
    def __init__(self):
        self.data = []
        self.processed = False
    
    def add_data(self, value):
        self.data.append(value)
        self.processed = False
    
    def process(self):
        # Some processing logic here
        self.processed = True 