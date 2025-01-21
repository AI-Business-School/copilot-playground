"""
Regex Helper Example

This file demonstrates how to use GitHub Copilot to generate and understand regex patterns.
Each pattern includes questions you can ask about validation, edge cases, and alternatives.
"""

import re
from typing import List, Optional
from datetime import datetime

class RegexHelper:
    """Collection of regex patterns and validation methods"""

    # TODO: Ask Copilot questions about email validation:
    # - What edge cases does this handle?
    # - How to validate international emails?
    # - What about plus addressing?
    # - Should we allow IP addresses?
    # - What are the RFC standards?
    EMAIL_PATTERN = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')

    # TODO: Ask Copilot questions about URL validation:
    # - How to handle different protocols?
    # - What about query parameters?
    # - Should we allow fragments?
    # - How to validate international URLs?
    # - What about security concerns?
    URL_PATTERN = re.compile(r'^(https?:\/\/)?([\da-z.-]+)\.([a-z.]{2,6})([\/\w .-]*)*\/?$')

    # TODO: Ask Copilot questions about password validation:
    # - What makes a strong password?
    # - How to check complexity?
    # - What about special characters?
    # - Should we limit length?
    # - What are NIST guidelines?
    PASSWORD_PATTERN = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$')

    # TODO: Ask Copilot questions about date validation:
    # - How to handle different formats?
    # - What about international dates?
    # - Should we validate leap years?
    # - How to handle timezones?
    # - What about ISO 8601?
    DATE_PATTERN = re.compile(r'^(\d{4})-(\d{2})-(\d{2})$')

    # TODO: Ask Copilot questions about phone validation:
    # - How to handle international numbers?
    # - What about extensions?
    # - Should we allow formatting?
    # - How to validate country codes?
    # - What about E.164 format?
    PHONE_PATTERN = re.compile(r'^\+?1?\d{9,15}$')

    @classmethod
    def validate_email(cls, email: Optional[str]) -> bool:
        """Validate email address format"""
        if not email:
            return False
        return bool(cls.EMAIL_PATTERN.match(email))

    @classmethod
    def validate_url(cls, url: Optional[str]) -> bool:
        """Validate URL format"""
        if not url:
            return False
        return bool(cls.URL_PATTERN.match(url))

    @classmethod
    def validate_password(cls, password: Optional[str]) -> bool:
        """Validate password strength"""
        if not password:
            return False
        return bool(cls.PASSWORD_PATTERN.match(password))

    @classmethod
    def validate_date(cls, date: Optional[str]) -> bool:
        """Validate date format and value"""
        if not date:
            return False
        match = cls.DATE_PATTERN.match(date)
        if not match:
            return False
        
        try:
            year, month, day = map(int, match.groups())
            d = datetime(year, month, day)
            return d.month == month and d.day == day
        except ValueError:
            return False

    @classmethod
    def validate_phone(cls, phone: Optional[str]) -> bool:
        """Validate phone number format"""
        if not phone:
            return False
        return bool(cls.PHONE_PATTERN.match(phone))

    @classmethod
    def find_emails(cls, text: Optional[str]) -> List[str]:
        """Find all email addresses in text"""
        if not text:
            return []
        return cls.EMAIL_PATTERN.findall(text)

    @classmethod
    def find_urls(cls, text: Optional[str]) -> List[str]:
        """Find all URLs in text"""
        if not text:
            return []
        return cls.URL_PATTERN.findall(text)

    @classmethod
    def format_phone(cls, phone: Optional[str]) -> str:
        """Format phone number consistently"""
        if not phone:
            return ''
        digits = re.sub(r'\D', '', phone)
        if len(digits) == 10:
            return re.sub(r'(\d{3})(\d{3})(\d{4})', r'(\1) \2-\3', digits)
        if len(digits) == 11:
            return re.sub(r'(\d{1})(\d{3})(\d{3})(\d{4})', r'+\1 (\2) \3-\4', digits)
        return phone

def run_examples():
    """Example usage of the regex patterns"""
    # Test email validation
    print('Email validation:')
    print('test@example.com ->', RegexHelper.validate_email('test@example.com'))
    print('invalid-email ->', RegexHelper.validate_email('invalid-email'))

    # Test URL validation
    print('\nURL validation:')
    print('https://example.com ->', RegexHelper.validate_url('https://example.com'))
    print('invalid-url ->', RegexHelper.validate_url('invalid-url'))

    # Test password validation
    print('\nPassword validation:')
    print('StrongPass1! ->', RegexHelper.validate_password('StrongPass1!'))
    print('weakpass ->', RegexHelper.validate_password('weakpass'))

    # Test date validation
    print('\nDate validation:')
    print('2024-03-15 ->', RegexHelper.validate_date('2024-03-15'))
    print('2024-13-45 ->', RegexHelper.validate_date('2024-13-45'))

    # Test phone validation
    print('\nPhone validation:')
    print('+1234567890 ->', RegexHelper.validate_phone('+1234567890'))
    print('invalid-phone ->', RegexHelper.validate_phone('invalid-phone'))

    # Test finding patterns in text
    text = 'Contact us at test@example.com or visit https://example.com'
    print('\nFind patterns:')
    print('Emails:', RegexHelper.find_emails(text))
    print('URLs:', RegexHelper.find_urls(text))

    # Test phone formatting
    print('\nPhone formatting:')
    print('1234567890 ->', RegexHelper.format_phone('1234567890'))
    print('11234567890 ->', RegexHelper.format_phone('11234567890'))

if __name__ == '__main__':
    run_examples()

# Practice exercises:
# TODO: Ask Copilot questions about these patterns
# 1. Credit card validation
# 2. IP address matching
# 3. Social security numbers
# 4. ISBN validation
# 5. Postal codes 

"""
Regex Pattern Exercises - Python Version

This file contains exercises for creating regular expressions with clear input/output examples.
Each exercise is designed to test the AI model's ability to understand requirements and generate correct patterns.
"""

import re

# Exercise 1: Capital Letter Words
# Input: "Hello World Python Programming"
# Output: ["Hello", "World", "Python", "Programming"]
# Description: Match all words that start with a capital letter
def find_capital_words(text):
    pattern = r'[A-Z][a-z]+'
    return re.findall(pattern, text)

# Exercise 2: Email Extraction
# Input: "Contact us at: support@example.com or sales.dept@company.co.uk"
# Output: ["support@example.com", "sales.dept@company.co.uk"]
# Description: Extract email addresses from text
def extract_emails(text):
    pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    return re.findall(pattern, text)

# Exercise 3: Date Format Validation
# Input: "2024-01-15" or "2024/01/15" or "15-01-2024"
# Output: True/False
# Description: Validate dates in multiple formats (YYYY-MM-DD, YYYY/MM/DD, DD-MM-YYYY)
def validate_date(date_string):
    pattern = r'^(?:\d{4}[-/]\d{2}[-/]\d{2}|\d{2}[-/]\d{2}[-/]\d{4})$'
    return bool(re.match(pattern, date_string))

# Exercise 4: Phone Number Format
# Input: "+1-555-123-4567" or "(555) 123-4567" or "555.123.4567"
# Output: True/False
# Description: Validate phone numbers in various formats
def validate_phone(phone):
    pattern = r'^\+?\d{1,3}[-.]?\(?(\d{3})\)?[-.]?\d{3}[-.]?\d{4}$'
    return bool(re.match(pattern, phone))

# Exercise 5: URL Components
# Input: "https://api.example.com/v1/users?id=123#profile"
# Output: {
#     "protocol": "https",
#     "domain": "api.example.com",
#     "path": "/v1/users",
#     "query": "id=123",
#     "fragment": "profile"
# }
# Description: Extract different components of a URL
def parse_url(url):
    pattern = r'^(?P<protocol>https?):\/\/(?P<domain>[^\/]+)(?P<path>\/[^?#]*)?(?:\?(?P<query>[^#]*))?(?:#(?P<fragment>.*))?$'
    match = re.match(pattern, url)
    return match.groupdict() if match else None

# Exercise 6: Password Strength
# Input: "MyP@ssw0rd123"
# Output: True/False
# Description: Validate password strength (min 8 chars, 1 uppercase, 1 lowercase, 1 number, 1 special char)
def validate_password(password):
    pattern = r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$'
    return bool(re.match(pattern, password))

# Exercise 7: Code Comment Extraction
# Input: "def hello(): # Say hello\\n    print('Hello') # Print greeting"
# Output: ["Say hello", "Print greeting"]
# Description: Extract single-line comments from Python code
def extract_comments(code):
    pattern = r'#\s*(.+)$'
    return re.findall(pattern, code, re.MULTILINE)

# Exercise 8: Version Number Parsing
# Input: "v1.2.3-alpha.1" or "2.0.0" or "1.0.0-beta"
# Output: {
#     "major": "1",
#     "minor": "2",
#     "patch": "3",
#     "label": "alpha.1"
# }
# Description: Parse semantic version numbers
def parse_version(version):
    pattern = r'^v?(?P<major>\d+)\.(?P<minor>\d+)\.(?P<patch>\d+)(?:-(?P<label>[a-zA-Z0-9.-]+))?$'
    match = re.match(pattern, version)
    return match.groupdict() if match else None

# Exercise 9: HTML Tag Extraction
# Input: "<div class='container'><p>Hello</p></div>"
# Output: ["div", "p"]
# Description: Extract HTML tag names
def extract_html_tags(html):
    pattern = r'<(\w+)[^>]*>'
    return re.findall(pattern, html)

# Exercise 10: Log Entry Parsing
# Input: "2024-01-15 10:30:45 [ERROR] Failed to connect: timeout"
# Output: {
#     "date": "2024-01-15",
#     "time": "10:30:45",
#     "level": "ERROR",
#     "message": "Failed to connect: timeout"
# }
# Description: Parse structured log entries
def parse_log_entry(log_line):
    pattern = r'^(?P<date>\d{4}-\d{2}-\d{2})\s+(?P<time>\d{2}:\d{2}:\d{2})\s+\[(?P<level>\w+)\]\s+(?P<message>.+)$'
    match = re.match(pattern, log_line)
    return match.groupdict() if match else None 