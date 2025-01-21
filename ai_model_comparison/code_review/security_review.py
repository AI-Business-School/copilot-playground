"""
Exercise: Security-Critical Code Review

Code for Review:
The following code implements a user authentication system with JWT tokens.
Review it for security issues, best practices, and potential improvements.

import jwt
import hashlib
from datetime import datetime, timedelta
from typing import Optional, Dict

class UserAuth:
    def __init__(self, db_connection, secret_key: str):
        self.db = db_connection
        self.secret = secret_key
        
    def authenticate_user(self, username: str, password: str) -> Optional[Dict]:
        # Hash password
        hashed_pass = hashlib.md5(password.encode()).hexdigest()
        
        # Query database
        user = self.db.execute(
            f"SELECT * FROM users WHERE username='{username}' AND password='{hashed_pass}'"
        )
        
        if user:
            return self.generate_token(user)
        return None
        
    def generate_token(self, user: Dict) -> Dict:
        # Create token
        token = jwt.encode(
            {
                'user_id': user['id'],
                'exp': datetime.utcnow() + timedelta(days=1),
                'role': user['role']
            },
            self.secret
        )
        
        # Store token
        self.db.execute(
            f"UPDATE users SET last_token='{token}' WHERE id={user['id']}"
        )
        
        return {'token': token}
        
    def validate_token(self, token: str) -> bool:
        try:
            decoded = jwt.decode(token, self.secret, algorithms=['HS256'])
            user = self.db.execute(
                f"SELECT last_token FROM users WHERE id={decoded['user_id']}"
            )
            return user and user['last_token'] == token
        except:
            return False

Review Requirements:
1. Security Analysis
   - Authentication mechanisms
   - Password handling
   - SQL injection vulnerabilities
   - Token management
   - Error handling

2. Code Quality
   - Code structure
   - Error handling
   - Type safety
   - Documentation
   - Testing considerations

3. Best Practices
   - Security best practices
   - Python coding standards
   - API design principles
   - Database interaction
   - Configuration management

4. Performance Considerations
   - Database queries
   - Token generation/validation
   - Memory usage
   - Scalability issues

Compare how each AI model:
- Identifies security vulnerabilities
- Suggests improvements
- Explains security implications
- Provides practical solutions
- Considers edge cases
- References relevant standards/best practices
""" 