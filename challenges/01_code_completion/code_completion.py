"""
Code Completion Examples
"""

from typing import List, TypeVar, Dict, Any

T = TypeVar('T')
Number = TypeVar('Number', int, float)

# Exercise 1: Easy
# Implement a method that finds the maximum value in a list
# Handle empty lists by returning None
def find_max(arr: List[Number]) -> Number:
    # your implementation here
    pass

# Exercise 2: Medium
# Implement a method that finds all duplicates in a list
# Example: find_duplicates([1, 2, 2, 3, 3, 4]) should return [2, 3]
def find_duplicates(arr: List[T]) -> List[T]:
    # your implementation here
    pass

# Exercise 3: Hard
# Implement a method that groups a list of dictionaries by a specified key
# Example: group_by_key([
#     {"type": "A", "value": 1}, 
#     {"type": "B", "value": 2}, 
#     {"type": "A", "value": 3}
# ], "type")
# Should return: {
#     "A": [{"type": "A", "value": 1}, {"type": "A", "value": 3}],
#     "B": [{"type": "B", "value": 2}]
# }
def group_by_key(items: List[Dict[str, Any]], key: str) -> Dict[str, List[Dict[str, Any]]]:
    # your implementation here
    pass

def run_examples():
    """Example usage of the functions"""
    numbers = [4, 2, 7, 1, 9, 5]
    print('Max:', find_max(numbers))
    print('Duplicates:', find_duplicates([1, 2, 2, 3, 3, 4]))
    items = [
        {"type": "A", "value": 1},
        {"type": "B", "value": 2},
        {"type": "A", "value": 3}
    ]
    print('Grouped by type:', group_by_key(items, "type"))

if __name__ == "__main__":
    run_examples()