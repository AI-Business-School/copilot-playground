# Regex Patterns Exercise Guideline

This document provides guidelines for practicing regex pattern generation with GitHub Copilot.

## [Objective]

- Learn how to generate regex patterns for common use cases
- Practice writing clear descriptions that lead to correct regex patterns
- Understand how to test and validate regex patterns
- Master common regex pattern techniques

## [Exercise Overview]

The exercises demonstrate four common regex pattern scenarios in both JavaScript and Python:

### 1. Email Validation Pattern

```javascript
// Pattern: ^[\w.-]+@[\w.-]+\.[a-zA-Z]{2,6}$
// Validates email addresses with these rules:
// - Contains exactly one @ symbol
// - Local part: letters, numbers, dots, underscores
// - Domain part: letters, numbers, dots, hyphens
// - TLD: 2-6 characters

// Test Cases:
✅ user@example.com
✅ user.name@sub.domain.com
❌ user@domain
❌ @domain.com
```

### 2. Phone Number Formatting

```python
# Pattern: (\d{3})(\d{3})(\d{4})
# Formats phone numbers:
# - Extracts 10 digits from input
# - Groups into area code, prefix, line number
# - Formats as (XXX) XXX-XXXX

# Test Cases:
✅ 1234567890 -> (123) 456-7890
✅ 123-456-7890 -> (123) 456-7890
❌ 12345 (too short)
❌ 12345678901 (too long)
```

### 3. URL Parsing

```javascript
// Pattern: ^(?:(?<protocol>https?):\/\/)?(?<domain>[\w.-]+)(?<path>\/[\w\/.-]*)?(?:\?(?<query>[\w=&]+))?$
// Parses URL components:
// - Protocol (optional): http or https
// - Domain (required): letters, numbers, dots, hyphens
// - Path (optional): starts with /, contains word chars, dots, slashes
// - Query (optional): starts with ?, contains word chars, =, &

// Test Cases:
✅ https://example.com
✅ example.com/path
✅ https://sub.domain.com/path?query=value
❌ ftp://example.com
```

### 4. Log Entry Parsing

```python
# Pattern: ^\[(?P<timestamp>\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})\] \[(?P<level>\w+)\] (?P<message>[^{]+)(?:\s*{(?P<metadata>.*)})?$
# Parses log entries with format:
# - Timestamp: [YYYY-MM-DD HH:MM:SS]
# - Level: [INFO|ERROR|WARN|DEBUG]
# - Message: any text
# - Metadata: optional {key=value} pairs

# Test Cases:
✅ [2024-01-30 14:30:00] [INFO] User logged in {user_id=123}
✅ [2024-01-30 14:30:00] [ERROR] Failed to connect
❌ [2024-01-30] [INFO] Invalid timestamp
```

## [Pattern Building Guidelines]

1. Start with Requirements Analysis:

   ```javascript
   // 1. Define what to match/exclude
   // 2. List all valid formats
   // 3. Identify optional components
   // 4. Note special characters
   ```

2. Break Down Complex Patterns:

   ```javascript
   // Email Pattern Breakdown:
   ^               // Start of string
   [\w.-]+        // Local part: word chars, dots, hyphens
   @              // Literal @ symbol
   [\w.-]+        // Domain: word chars, dots, hyphens
   \.             // Literal dot
   [a-zA-Z]{2,6}  // TLD: 2-6 letters
   $              // End of string
   ```

3. Use Named Groups for Clarity:

   ```python
   # JavaScript: (?<name>pattern)
   # Python: (?P<name>pattern)
   pattern = r'^(?P<protocol>https?):\/\/(?P<domain>[\w.-]+)'
   ```

4. Handle Special Cases:
   ```javascript
   // 1. Optional components: (?:pattern)?
   // 2. Character escaping: \. \/ \?
   // 3. Character classes: \w \d \s
   // 4. Quantifiers: + * {n,m}
   ```

## [Language-Specific Considerations]

1. JavaScript:

   ```javascript
   // Using RegExp
   const pattern = /regex/flags;
   const pattern = new RegExp('regex', 'flags');

   // Common Methods
   pattern.test(string)     // Returns boolean
   string.match(pattern)    // Returns match array
   string.replace(pattern)  // Returns modified string
   ```

2. Python:

   ```python
   # Using re module
   import re
   pattern = r'regex'  # r prefix for raw string

   # Common Methods
   re.match(pattern, string)   // Match at start
   re.search(pattern, string)  // Match anywhere
   re.sub(pattern, repl, string)  // Replace matches
   ```

## [Testing Strategies]

1. Test Case Categories:

   ```javascript
   // Valid Cases
   - Standard formats
   - Edge cases within limits
   - Optional components

   // Invalid Cases
   - Missing required parts
   - Invalid characters
   - Wrong format/order
   ```

2. Performance Testing:
   ```javascript
   // Check regex efficiency
   - Avoid catastrophic backtracking
   - Test with large inputs
   - Monitor execution time
   ```

## [Practice Exercise]

1. Choose a pattern type:

   - Data validation (email, phone, dates)
   - Format parsing (logs, URLs, files)
   - Text extraction (tags, quotes, code)
   - Custom formats

2. Development Steps:

   - Write requirements
   - List test cases
   - Build pattern incrementally
   - Test and refine
   - Document with examples

3. Implementation:
   - Start with basic pattern
   - Add capture groups
   - Handle edge cases
   - Add validation
   - Write clear documentation

## [Best Practices]

1. Start with simple patterns and build up complexity
2. Use named capture groups for clarity
3. Consider performance implications
4. Add comments to explain complex patterns
5. Test with a variety of inputs
6. Consider different regex engine implementations

## [Examples]

See `regex_patterns.js` and `regex_patterns.py` for practical examples of:

- Email validation
- Phone number matching
- URL parsing
- Date format validation
- Custom format matching
