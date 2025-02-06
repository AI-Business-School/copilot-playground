# Code Completion Exercise Guideline

This document provides guidelines for creating code completion exercises that demonstrate GitHub Copilot's capabilities.

## [Objective]

- Learn how to use GitHub Copilot to complete partial implementations.
- Practice writing guiding code that helps Copilot understand your intent.
- Understand how different comment styles affect Copilot's suggestions.
- Explore variations of implementations for common algorithms.

## [Exercise Overview]

The exercises include common programming tasks in both JavaScript and Python:

### JavaScript Examples (`code_completion.js`):

```javascript
-findMaxValue(arr) - // Find the maximum value in an array
  findDuplicates(arr) - // Find duplicate elements in an array
  groupByProperty(arr, property); // Group array objects by a specific property
```

### Python Examples (`code_completion.py`):

```python
- find_max(arr: List[Number]) -> Number  # Type-safe maximum value finder
- find_duplicates(arr: List[T]) -> List[T]  # Generic duplicate finder
- group_by_key(items: List[Dict], key: str) -> Dict  # Dictionary grouping
```

## [GitHub Copilot Best Practices]

1. Write clear and descriptive comments above functions
2. Use type hints/annotations:
   - Python: Leverage `typing` module (List, Dict, TypeVar)
   - JavaScript: Use JSDoc type annotations
3. Start with a good function signature:
   - Use descriptive parameter names
   - Include return type information
4. Break down complex tasks into smaller functions
5. Use natural language descriptions in comments
6. Include example inputs/outputs in comments:
   ```python
   # Example:
   # Input: [1, 2, 2, 3, 4, 4, 5]
   # Output: [2, 4]
   ```

## [Working with Copilot]

1. Press Ctrl+Enter (Windows/Linux) or Cmd+Enter (Mac) to see alternative suggestions
2. Use inline comments to guide suggestions:
   ```javascript
   // First, create a frequency map
   // Then, filter elements with count > 1
   ```
3. Add docstrings/JSDoc comments for better context:
   ```javascript
   /**
    * Finds duplicate elements in an array
    * @param {Array} arr - The input array
    * @returns {Array} - Array of duplicate elements
    */
   ```
4. Test different comment styles:
   - Single-line comments for step-by-step guidance
   - Multi-line comments for detailed explanations
   - Type annotations for precise implementations
5. Use // to continue generating more code

## [Instructions]

1. Choose your preferred language (JavaScript or Python)
2. Open the corresponding file (`code_completion.js` or `code_completion.py`)
3. Use the "Edit with Copilot" feature (Cmd/Ctrl + I)
4. Try these approaches for each function:
   a. Add only type hints and let Copilot suggest implementation
   b. Write descriptive comments about the algorithm
   c. Include example inputs/outputs
   d. Mix different styles to see what works best
5. Review and modify Copilot's suggestions as needed
6. Test the implementations with various inputs

## [Example Workflow]

1. Start with `findMaxValue`/`find_max`:

   ```javascript
   /**
    * Finds the maximum value in an array of numbers
    * @example
    * Input: [1, 5, 3, 9, 2]
    * Output: 9
    */
   function findMaxValue(arr) {
     // your implementation here
   }
   ```

2. Let Copilot suggest implementation
3. Try alternative approaches:
   - Using reduce method
   - Using Math.max with spread
   - Using traditional loop
4. Repeat for other functions with increasing complexity
