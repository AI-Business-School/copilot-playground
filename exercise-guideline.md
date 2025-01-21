# Exercise Creation Guidelines

This document provides guidelines for creating new exercises that demonstrate GitHub Copilot's capabilities. Follow these guidelines to maintain consistency and educational value across all exercises.

## 🎯 Exercise Structure

Each exercise should follow this basic structure:

1. **Topic Directory**

   ```
   challenges/
   └── XX_topic_name/
       ├── README.md
       ├── javascript/
       │   └── exercise_file.js
       └── python/
           └── exercise_file.py
   ```

2. **File Components**
   - README.md: Topic overview and learning objectives
   - Language-specific implementations with strategic gaps
   - Example outputs and challenges

## 📝 Exercise Types and Empty Sections

Choose one of these exercise types and leave appropriate sections empty:

1. **Code Completion**

   - Provide method signatures and documentation
   - Leave implementation body empty
   - Include TODO comments for Copilot

   ```javascript
   function processArray(arr) {
     // TODO: Implement array processing using GitHub Copilot
     // Your implementation here...
   }
   ```

2. **Comment to Code**

   - Write detailed comments about functionality
   - Leave entire implementation empty
   - Show example input/output

   ```javascript
   /**
    * Transforms input array by:
    * 1. Filtering out nulls
    * 2. Mapping values to their square
    * 3. Sorting in descending order
    *
    * Input: [1, null, 3, 2]
    * Output: [9, 4, 1]
    */
   function transformArray(arr) {
     // Your implementation here...
   }
   ```

3. **Code to Comment**

   - Provide complex implementation
   - Leave documentation sections empty
   - Include comment placeholders

   ```javascript
   // TODO: Document this function using GitHub Copilot
   function processData(input) {
     const validated = validate(input);
     const transformed = transform(validated);
     return format(transformed);
   }
   ```

4. **Type Hinting**

   - Provide implementation
   - Leave type definitions empty
   - Include type hint placeholders

   ```typescript
   // TODO: Add type definitions using GitHub Copilot
   function processUser(/* Add types */) {
     // Implementation...
   }
   ```

5. **Showing Examples**
   - Show example input/output
   - Leave implementation empty
   - Include test cases
   ```javascript
   /**
    * Example Input: { name: "John", age: 30 }
    * Example Output: "Name: John, Age: 30 years"
    */
   function formatUser(user) {
     // Your implementation here...
   }
   ```

## 💡 Best Practices for Empty Sections

1. **Strategic Gaps**

   ```javascript
   class DataProcessor {
     // Provided: Basic structure and types
     constructor(config) {
       this.config = config;
     }

     // Empty: Complex processing logic
     processData(input) {
       // TODO: Implement data processing using GitHub Copilot
       // Your implementation here...
     }

     // Provided: Helper methods
     validate(data) {
       return data != null;
     }
   }
   ```

2. **Progressive Implementation**

   ```javascript
   // 1. Start with basic implementation (provided)
   function basicTransform(data) {
     return data.map((item) => item * 2);
   }

   // 2. Add validation (empty for user)
   function validateInput(data) {
     // TODO: Implement validation using GitHub Copilot
     // Your implementation here...
   }

   // 3. Implement advanced features (empty for user)
   function advancedTransform(data, options) {
     // TODO: Implement advanced transformation using GitHub Copilot
     // Your implementation here...
   }
   ```

3. **Guided Comments**
   ```javascript
   /**
    * TODO: Complete each step using GitHub Copilot
    *
    * Step 1: Validate input
    * - Check for null/undefined
    * - Verify array structure
    *
    * Step 2: Transform data
    * - Apply mapping function
    * - Handle edge cases
    *
    * Step 3: Format output
    * - Convert to required structure
    * - Add metadata
    */
   ```

## 🔍 Exercise Components with Empty Sections

1. **Challenge Structure**

   ```javascript
   class Challenge {
     // Provided: Interface and types
     constructor() {
       this.data = [];
     }

     // Empty: Core functionality
     process() {
       // TODO: Implement using GitHub Copilot
       // Your implementation here...
     }

     // Provided: Example usage
     static example() {
       const challenge = new Challenge();
       return challenge.process([1, 2, 3]);
     }
   }
   ```

2. **Test Cases**

   ```javascript
   // Provided: Basic test cases
   assert(processData(null) === defaultValue);

   // Empty: Advanced test cases
   // TODO: Add edge case tests using GitHub Copilot
   // Your test cases here...
   ```

## 📚 Topics to Cover

1. **Data Transformation**

   - Provide basic transformations
   - Leave complex mappings empty
   - Include edge cases

2. **Pattern Implementation**

   - Show pattern structure
   - Leave implementation details empty
   - Provide usage examples

3. **API Integration**

   - Define API interfaces
   - Leave request handling empty
   - Show response formats

4. **Validation & Sanitization**
   - Define validation rules
   - Leave validation logic empty
   - Include test cases

## ✅ Quality Checklist for Empty Sections

1. **Documentation**

   - [ ] Clear instructions for empty sections
   - [ ] Well-defined requirements
   - [ ] Helpful hints and examples

2. **Implementation**

   - [ ] Strategic empty sections
   - [ ] Clear TODO comments
   - [ ] Sufficient context for Copilot

3. **Educational Value**

   - [ ] Progressive difficulty in empty sections
   - [ ] Clear learning path
   - [ ] Meaningful challenges

4. **Testing**
   - [ ] Test cases for empty sections
   - [ ] Validation criteria
   - [ ] Expected outcomes

## 🚀 Contributing

When creating new exercises:

1. Identify appropriate sections to leave empty
2. Provide clear context for Copilot
3. Include example solutions separately
4. Test with Copilot before submitting

Remember to:

- Balance provided code and empty sections
- Include clear hints in comments
- Provide sufficient context for Copilot
- Test that Copilot can effectively complete the empty sections
