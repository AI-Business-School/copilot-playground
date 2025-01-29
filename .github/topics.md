## 📚 Topics to Cover

#"challenges" folder

1. **Code Completion**

   - Provide method signatures and documentation
   - Leave implementation body empty
   - Include DO_WITH_COPILOT comments for Copilot

2. **Comment to Code**

   - Write detailed comments about functionality
   - Leave entire implementation empty
   - Show example input/output

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
