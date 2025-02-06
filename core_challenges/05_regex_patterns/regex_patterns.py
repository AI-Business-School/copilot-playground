import re

# Example 1: Email Validation
def validate_email(email: str) -> bool:
    """
    Create a regex pattern that validates email addresses with the following rules:
    - Contains exactly one @ symbol
    - Local part can contain letters, numbers, dots, and underscores
    - Domain part can contain letters, numbers, dots, and hyphens
    - Must end with a valid TLD (2-6 characters)
    """
    pattern = r'^[\w.-]+@[\w.-]+\.[a-zA-Z]{2,6}$'
    return bool(re.match(pattern, email))

# Example 2: Phone Number Format
def format_phone_number(phone: str) -> str:
    """
    Create a regex pattern that formats phone numbers:
    - Input can be any string of 10 digits
    - Output should be in format: (XXX) XXX-XXXX
    - Should handle inputs with or without existing formatting
    """
    # First remove all non-digit characters
    digits_only = re.sub(r'\D', '', phone)
    if len(digits_only) != 10:
        raise ValueError("Phone number must contain exactly 10 digits")
    
    pattern = r'(\d{3})(\d{3})(\d{4})'
    return re.sub(pattern, r'(\1) \2-\3', digits_only)

# Example 3: URL Parser
def parse_url(url: str) -> dict:
    """
    Create a regex pattern that parses URLs into components:
    - Protocol (optional, defaults to http)
    - Domain (required)
    - Path (optional)
    - Query parameters (optional)
    """
    pattern = r'^(?:(?P<protocol>https?):\/\/)?(?P<domain>[\w.-]+)(?P<path>\/[\w\/.-]*)?(?:\?(?P<query>[\w=&]+))?$'
    match = re.match(pattern, url)
    if not match:
        raise ValueError("Invalid URL format")
    
    return match.groupdict()

# Example 4: Custom Log Format
def parse_log_entry(log_line: str) -> dict:
    """
    Create a regex pattern that parses log entries with format:
    [YYYY-MM-DD HH:MM:SS] [LEVEL] Message (optional: {key1=value1, key2=value2})
    Example: [2024-01-30 14:30:00] [INFO] User logged in {user_id=123, ip=192.168.1.1}
    """
    pattern = r'^\[(?P<timestamp>\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})\] \[(?P<level>\w+)\] (?P<message>[^{]+)(?:\s*{(?P<metadata>.*)})?$'
    match = re.match(pattern, log_line)
    if not match:
        raise ValueError("Invalid log format")
    
    result = match.groupdict()
    if result['metadata']:
        metadata = {}
        for pair in result['metadata'].split(','):
            key, value = pair.strip().split('=')
            metadata[key.strip()] = value.strip()
        result['metadata'] = metadata
    return result 