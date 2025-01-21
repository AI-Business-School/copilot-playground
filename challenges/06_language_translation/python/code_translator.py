"""
Code Translation Example
This file demonstrates GitHub Copilot's ability to translate code between languages.

Try the following:
1. Type a comment with the code you want to translate
2. Specify the target language
3. Let Copilot generate the translated code
"""

from typing import List, TypeVar, Callable, Any, Optional
from dataclasses import dataclass
from functools import wraps
import asyncio
import aiofiles
import time

T = TypeVar('T')

class CodeTranslator:
    """A class demonstrating code translation between languages."""

    @staticmethod
    def list_comprehension(numbers: List[int]) -> List[int]:
        """
        Demonstrates translating JavaScript array methods to Python.
        JavaScript:
        numbers
            .filter(x => x > 0)
            .map(x => x * 2);
        
        Args:
            numbers (List[int]): List of numbers to process
            
        Returns:
            List[int]: Processed numbers
        """
        return [x * 2 for x in numbers if x > 0]

    @staticmethod
    async def with_file_handling(filename: str) -> str:
        """
        Demonstrates translating JavaScript try-finally to Python context manager.
        JavaScript:
        let fileHandle;
        try {
            fileHandle = await fs.promises.open(filename, 'r');
            const content = await fileHandle.readFile('utf8');
            return content;
        } finally {
            if (fileHandle) await fileHandle.close();
        }
        
        Args:
            filename (str): Name of the file to read
            
        Returns:
            str: Content of the file
        """
        async with aiofiles.open(filename, 'r') as file:
            return await file.read()

    @staticmethod
    def retry(max_attempts: int, delay: int) -> Callable:
        """
        Demonstrates translating JavaScript higher-order functions to Python decorators.
        JavaScript:
        function retry(maxAttempts, delay) {
            return function(target) {
                return async function(...args) {
                    // ... implementation
                }
            }
        }
        
        Args:
            max_attempts (int): Maximum number of retry attempts
            delay (int): Delay between attempts in seconds
            
        Returns:
            Callable: Decorator function
        """
        def decorator(func: Callable) -> Callable:
            @wraps(func)
            async def wrapped(*args: Any, **kwargs: Any) -> Any:
                last_error: Optional[Exception] = None
                for attempt in range(1, max_attempts + 1):
                    try:
                        return await func(*args, **kwargs)
                    except Exception as error:
                        last_error = error
                        if attempt < max_attempts:
                            await asyncio.sleep(delay)
                if last_error:
                    raise last_error
            return wrapped
        return decorator

# Example usage:
async def main():
    # List comprehension example
    numbers = [-2, -1, 0, 1, 2, 3]
    print('List comprehension:', 
        CodeTranslator.list_comprehension(numbers))

    # Using the retry decorator
    @CodeTranslator.retry(max_attempts=3, delay=1)
    async def fetch_data():
        """Simulated API call that might fail."""
        # In a real application, use aiohttp or httpx for HTTP requests
        await asyncio.sleep(0.1)  # Simulate network delay
        return {'data': 'success'}

    try:
        result = await fetch_data()
        print('Fetch result:', result)
    except Exception as e:
        print('Error:', e)

if __name__ == '__main__':
    asyncio.run(main())

# Challenges:
# 1. Translate JavaScript's Promise.all to Python asyncio.gather
# 2. Convert JavaScript's class fields to Python dataclasses
# 3. Implement JavaScript's array spread operator in Python 