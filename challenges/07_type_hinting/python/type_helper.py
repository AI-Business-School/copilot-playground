"""
Type Hinting Example

This file demonstrates how to use GitHub Copilot for type hinting.
Each section contains types and protocols that you can ask questions about.
"""

from typing import TypeVar, Generic, Dict, List, Optional, Union, Protocol, TypedDict, NewType, Any
from dataclasses import dataclass
from datetime import datetime
import uuid

# Basic Types and Classes
UserId = NewType('UserId', str)
Role = Union['admin', 'user', 'guest']

@dataclass
class UserPreferences:
    theme: str
    notifications: bool
    language: str

@dataclass
class User:
    id: UserId
    name: str
    email: str
    role: Role
    preferences: Optional[UserPreferences]
    created_at: datetime
    updated_at: datetime

# Generic Types and Protocols
T = TypeVar('T', bound='HasId')

class HasId(Protocol):
    id: str

class Repository(Generic[T]):
    """
    TODO: Ask Copilot questions about Repository implementation:
    - How to handle type constraints?
    - What about error handling?
    - Should we use generics?
    - How to implement caching?
    - What about transaction support?
    """
    def __init__(self, name: str, validate: callable):
        self.name = name
        self.validate = validate
        self.store: Dict[str, T] = {}

    async def find_by_id(self, id: str) -> Optional[T]:
        return self.store.get(id)

    async def find_all(self) -> List[T]:
        return list(self.store.values())

    async def create(self, item: Dict) -> T:
        id = str(uuid.uuid4())
        new_item = {**item, 'id': id}
        if not self.validate(new_item):
            raise ValueError('Invalid item')
        self.store[id] = new_item  # type: ignore
        return new_item  # type: ignore

    async def update(self, id: str, item: Dict) -> T:
        existing = self.store.get(id)
        if not existing:
            raise ValueError('Item not found')
        updated = {**existing, **item}  # type: ignore
        if not self.validate(updated):
            raise ValueError('Invalid item')
        self.store[id] = updated  # type: ignore
        return updated  # type: ignore

    async def delete(self, id: str) -> bool:
        if id in self.store:
            del self.store[id]
            return True
        return False

# Union Types and Type Guards
class Success(TypedDict):
    success: bool
    data: Any

class Failure(TypedDict):
    success: bool
    error: Exception

Result = Union[Success, Failure]

class TypeHelper:
    """Collection of type-safe utilities"""

    @staticmethod
    async def handle_result(promise: callable) -> Result:
        """
        TODO: Ask Copilot questions about Result handling:
        - How to handle async operations?
        - What about type inference?
        - Should we use type guards?
        - How to chain results?
        - What about error types?
        """
        try:
            data = await promise()
            return {'success': True, 'data': data}
        except Exception as error:
            return {'success': False, 'error': error}

    @staticmethod
    def create_type_guard(check: callable) -> callable:
        """
        TODO: Ask Copilot questions about type guards:
        - When to use type predicates?
        - How to narrow union types?
        - What about branded types?
        - Should we use assertions?
        - How to handle unknown types?
        """
        def guard(value: Any) -> bool:
            try:
                return check(value)
            except:
                return False
        return guard

    @staticmethod
    def create_type_mapper(transform: callable) -> callable:
        """
        TODO: Ask Copilot questions about type mapping:
        - How to transform types?
        - What about conditional types?
        - Should we use template literals?
        - How to handle recursion?
        - What about type inference?
        """
        def mapper(items: List[Any]) -> List[Any]:
            return [transform(item) for item in items]
        return mapper

async def run_examples():
    """Example usage of the type helpers"""
    # Create a user repository
    def validate_user(user: Dict) -> bool:
        return (
            isinstance(user.get('id'), str) and
            isinstance(user.get('name'), str) and
            isinstance(user.get('email'), str) and
            user.get('role') in ['admin', 'user', 'guest']
        )

    user_repo = Repository[User]('users', validate_user)

    # Test result handling
    result = await TypeHelper.handle_result(
        lambda: user_repo.create({
            'name': 'Alice',
            'email': 'alice@example.com',
            'role': 'user',
            'created_at': datetime.now(),
            'updated_at': datetime.now()
        })
    )

    if result['success']:
        print('Created user:', result['data'])
    else:
        print('Error:', result['error'])

    # Test type guard
    is_user = TypeHelper.create_type_guard(
        lambda value: (
            isinstance(value, dict) and
            'id' in value and
            'name' in value and
            'email' in value
        )
    )

    unknown_value = {'id': '1', 'name': 'Bob', 'email': 'bob@example.com'}
    if is_user(unknown_value):
        print('Valid user:', unknown_value['name'])

    # Test type mapper
    to_user_dto = TypeHelper.create_type_mapper(
        lambda user: {'name': user['name'], 'email': user['email']}
    )

    users = await user_repo.find_all()
    dtos = to_user_dto(users)
    print('User DTOs:', dtos)

if __name__ == '__main__':
    import asyncio
    asyncio.run(run_examples())

# Practice exercises:
# TODO: Ask Copilot questions about these patterns
# 1. Protocol types
# 2. Type variables
# 3. Overload methods
# 4. Generic types
# 5. Type aliases 