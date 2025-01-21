# Showing Examples

This directory demonstrates how to use GitHub Copilot to generate code based on examples. The examples focus on providing clear examples that guide Copilot in generating similar code patterns, encouraging interactive learning through example-based development.

## Learning Objectives

1. Learn how to write effective examples that guide code generation
2. Understand how different example formats influence generated code
3. Practice implementing code based on example outputs
4. Develop skills in pattern recognition and replication

## Directory Structure

```
javascript/
└── example_generator.js    # JavaScript implementation with example-based patterns
python/
└── example_generator.py    # Python implementation with example-based patterns
```

## Examples

The examples demonstrate several patterns for example-based code generation:

1. Blog Post Generation

   ```json
   {
     "id": "post-123",
     "title": "Hello World",
     "content": "This is my first post",
     "author": {
       "id": "user-456",
       "name": "John Doe"
     },
     "tags": ["intro", "blog"],
     "createdAt": "2024-01-20T10:00:00Z"
   }
   ```

2. CSV Conversion

   ```
   Input:
   [
     { id: 1, name: "John", age: 30 },
     { id: 2, name: "Jane", age: 25 }
   ]
   Output:
   "id,name,age
   1,John,30
   2,Jane,25"
   ```

3. HTML Generation

   ```html
   <div class="profile-card">
     <img
       src="https://example.com/avatar.jpg"
       alt="John Doe"
       class="profile-image"
     />
     <h2 class="profile-name">John Doe</h2>
     <p class="profile-title">Software Engineer</p>
     <div class="profile-skills">
       <span class="skill-tag">JavaScript</span>
       <span class="skill-tag">Python</span>
     </div>
   </div>
   ```

4. SQL Generation
   ```sql
   Input:
   {
     tableName: 'users',
     fields: ['id', 'name', 'role'],
     conditions: { role: ['admin', 'user'], active: true }
   }
   Output:
   SELECT id, name, role FROM users WHERE role IN ('admin', 'user') AND active = true
   ```

## Practice Exercises

1. XML Generation

   ```xml
   <!-- Generate code that produces this XML -->
   <library>
     <book category="fiction">
       <title>The Great Gatsby</title>
       <author>F. Scott Fitzgerald</author>
       <year>1925</year>
     </book>
   </library>
   ```

2. GraphQL Schema

   ```graphql
   # Generate schema from this query
   query {
     user(id: "123") {
       name
       email
       posts {
         title
         content
       }
     }
   }
   ```

3. API Response
   ```json
   // Generate code that produces this response
   {
     "status": "success",
     "data": {
       "users": [
         { "id": 1, "name": "John" },
         { "id": 2, "name": "Jane" }
       ],
       "total": 2,
       "page": 1
     }
   }
   ```

## Tips for Better Examples

1. Structure

   - Show complete examples with all required fields
   - Include edge cases and special conditions
   - Demonstrate input/output relationships
   - Use realistic data values

2. Format

   - Follow language-specific conventions
   - Use consistent formatting
   - Include type information
   - Show validation rules

3. Documentation
   - Explain requirements clearly
   - List expected behaviors
   - Document edge cases
   - Provide test cases

## What to Observe

1. Example Influence

   - How example format affects output
   - Impact of example complexity
   - Role of type information
   - Effect of edge cases

2. Code Generation

   - Pattern recognition
   - Type inference
   - Error handling
   - Edge case handling

3. Implementation
   - Code structure
   - Validation rules
   - Error messages
   - Test coverage

## Learning Exercises

1. Example Writing

   - Write clear examples
   - Include edge cases
   - Show validation rules
   - Provide test data

2. Implementation

   - Follow example patterns
   - Handle edge cases
   - Add validation
   - Write tests

3. Pattern Recognition

   - Identify common patterns
   - Extract shared logic
   - Reuse patterns
   - Optimize code

4. Documentation
   - Document requirements
   - Explain patterns
   - Show usage
   - List limitations
