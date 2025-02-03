import unittest
from typing import List, Dict, Optional
from unittest.mock import Mock, patch
from datetime import datetime

# Code to be tested
class UserManager:
    def __init__(self, database):
        self.db = database
        self.active_users = set()

    def add_user(self, username: str, email: str) -> Dict:
        """
        Adds a new user to the system.
        Write tests that:
        - Verify successful user creation
        - Handle duplicate usernames
        - Validate email format
        - Mock database interactions
        """
        if not self._is_valid_email(email):
            raise ValueError("Invalid email format")
        
        if self._user_exists(username):
            raise ValueError("Username already exists")
        
        user = {
            'username': username,
            'email': email,
            'created_at': datetime.now(),
            'active': True
        }
        
        user_id = self.db.insert('users', user)
        user['id'] = user_id
        self.active_users.add(username)
        return user

    def _is_valid_email(self, email: str) -> bool:
        return '@' in email and '.' in email.split('@')[1]

    def _user_exists(self, username: str) -> bool:
        return self.db.exists('users', {'username': username})

    def get_user_stats(self) -> Dict:
        """
        Calculates user statistics.
        Write tests that:
        - Verify correct statistics calculation
        - Handle empty user database
        - Test performance with large datasets
        """
        total_users = self.db.count('users')
        active_users = len(self.active_users)
        return {
            'total_users': total_users,
            'active_users': active_users,
            'inactive_users': total_users - active_users
        }

class DataProcessor:
    def process_numbers(self, numbers: List[int]) -> Dict[str, float]:
        """
        Processes a list of numbers and returns statistics.
        Write tests that:
        - Verify correct calculations
        - Handle empty lists
        - Test with negative numbers
        - Check for numerical precision
        """
        if not numbers:
            raise ValueError("Input list cannot be empty")
        
        return {
            'sum': sum(numbers),
            'average': sum(numbers) / len(numbers),
            'min': min(numbers),
            'max': max(numbers)
        }

    def filter_data(self, items: List[Dict], criteria: Dict) -> List[Dict]:
        """
        Filters a list of dictionaries based on given criteria.
        Write tests that:
        - Verify correct filtering
        - Handle missing keys
        - Test with empty input
        - Check complex criteria
        """
        if not items or not criteria:
            return []
        
        result = []
        for item in items:
            matches = True
            for key, value in criteria.items():
                if key not in item or item[key] != value:
                    matches = False
                    break
            if matches:
                result.append(item)
        return result

# Write your tests here
class TestUserManager(unittest.TestCase):
    """Write comprehensive unit tests for the UserManager class"""
    pass

class TestDataProcessor(unittest.TestCase):
    """Write comprehensive unit tests for the DataProcessor class"""
    pass 