/**
 * Code Translation Example
 * This file demonstrates GitHub Copilot's ability to translate code between languages.
 * 
 * Try the following:
 * 1. Type a comment with the code you want to translate
 * 2. Specify the target language
 * 3. Let Copilot generate the translated code
 */

class CodeTranslator {
    /**
     * Demonstrates translating a Python list comprehension to JavaScript.
     * Python: [x * 2 for x in numbers if x > 0]
     */
    static listComprehension(numbers) {
        return numbers
            .filter(x => x > 0)
            .map(x => x * 2);
    }

    /**
     * Demonstrates translating Python's context manager (with statement)
     * Python:
     * with open('file.txt', 'r') as file:
     *     content = file.read()
     */
    static async withFileHandling(filename) {
        let fileHandle;
        try {
            fileHandle = await require('fs').promises.open(filename, 'r');
            const content = await fileHandle.readFile('utf8');
            return content;
        } finally {
            if (fileHandle) await fileHandle.close();
        }
    }

    /**
     * Demonstrates translating Python's decorators to JavaScript.
     * Python:
     * @retry(max_attempts=3, delay=1)
     * def fetch_data():
     *     ...
     */
    static retry(maxAttempts, delay) {
        return function decorator(target) {
            return async function wrapped(...args) {
                let lastError;
                for (let attempt = 1; attempt <= maxAttempts; attempt++) {
                    try {
                        return await target.apply(this, args);
                    } catch (error) {
                        lastError = error;
                        if (attempt < maxAttempts) {
                            await new Promise(resolve => 
                                setTimeout(resolve, delay * 1000));
                        }
                    }
                }
                throw lastError;
            };
        };
    }
}

// Example usage:
const numbers = [-2, -1, 0, 1, 2, 3];
console.log('List comprehension:', 
    CodeTranslator.listComprehension(numbers));

// Using the retry decorator
const fetchData = CodeTranslator.retry(3, 1)(async () => {
    const response = await fetch('https://api.example.com/data');
    return response.json();
});

// Challenges:
// 1. Translate Python's generator expressions to JavaScript
// 2. Convert Ruby's block syntax to JavaScript callbacks
// 3. Implement Python's dataclasses in JavaScript

module.exports = CodeTranslator; 