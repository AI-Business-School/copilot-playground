# Unit Testing Exercise Guideline

This document provides guidelines for creating comprehensive unit tests using GitHub Copilot.

## [Objective]

- Learn how to write effective unit tests for different types of code
- Practice test case design and coverage analysis
- Understand mocking and test isolation
- Master testing best practices and patterns

## [Exercise Overview]

The exercises demonstrate unit testing for two main classes in both JavaScript and Python:

### 1. UserManager Class Testing

````javascript
class UserManager {
    // Methods to test:
    async addUser(username, email)      // User creation with validation
    async getUserStats()                // Statistics calculation
    _isValidEmail(email)               // Email validation helper
    _userExists(username)              // Username existence check
}

// Test Categories:
1. User Creation Tests:
   ```javascript
   // Test successful user creation
   test('should create new user with valid details', async () => {
     const user = await userManager.addUser('john', 'john@example.com');
     expect(user).toHaveProperty('id');
     expect(user.username).toBe('john');
   });

   // Test duplicate username
   test('should reject duplicate username', async () => {
     await expect(userManager.addUser('existing', 'test@example.com'))
       .rejects.toThrow('Username already exists');
   });
````

2. Email Validation Tests:

   ```javascript
   test("should validate email format", () => {
     expect(userManager._isValidEmail("valid@example.com")).toBe(true);
     expect(userManager._isValidEmail("invalid-email")).toBe(false);
   });
   ```

3. Statistics Tests:
   ```javascript
   test("should calculate correct user statistics", async () => {
     const stats = await userManager.getUserStats();
     expect(stats).toHaveProperty("totalUsers");
     expect(stats).toHaveProperty("activeUsers");
   });
   ```

### 2. DataProcessor Class Testing

```python
class DataProcessor:
    def process_numbers(self, numbers: List[int])  # Statistical calculations
    def filter_data(self, items: List[Dict], criteria: Dict)  # Data filtering
```

1. Number Processing Tests:

   ```python
   def test_process_numbers_valid_input(self):
       processor = DataProcessor()
       result = processor.process_numbers([1, 2, 3, 4, 5])
       self.assertEqual(result['sum'], 15)
       self.assertEqual(result['average'], 3.0)
       self.assertEqual(result['min'], 1)
       self.assertEqual(result['max'], 5)
   ```

2. Data Filtering Tests:
   ```python
   def test_filter_data_with_criteria(self):
       items = [{'id': 1, 'status': 'active'}, {'id': 2, 'status': 'inactive'}]
       result = processor.filter_data(items, {'status': 'active'})
       self.assertEqual(len(result), 1)
       self.assertEqual(result[0]['id'], 1)
   ```

## [Test Design Patterns]

1. Arrange-Act-Assert Pattern:

   ```javascript
   describe("UserManager", () => {
     // Arrange
     let userManager;
     let mockDb;

     beforeEach(() => {
       mockDb = {
         insert: jest.fn(),
         exists: jest.fn(),
         count: jest.fn(),
       };
       userManager = new UserManager(mockDb);
     });

     test("addUser success", async () => {
       // Arrange
       mockDb.exists.mockResolvedValue(false);
       mockDb.insert.mockResolvedValue(1);

       // Act
       const result = await userManager.addUser("test", "test@example.com");

       // Assert
       expect(result).toHaveProperty("id", 1);
     });
   });
   ```

2. Mocking Dependencies:

   ```python
   @patch('database.Database')
   def test_user_creation(self, mock_db):
       # Configure mock
       mock_db.exists.return_value = False
       mock_db.insert.return_value = 1

       # Use mock in test
       manager = UserManager(mock_db)
       result = manager.add_user('test', 'test@example.com')
   ```

3. Edge Case Testing:

   ```javascript
   // Empty input handling
   test("should throw error for empty numbers array", () => {
     expect(() => processor.processNumbers([])).toThrow(
       "Input array cannot be empty"
     );
   });

   // Boundary testing
   test("should handle minimum/maximum values", () => {
     const result = processor.processNumbers([
       Number.MIN_SAFE_INTEGER,
       Number.MAX_SAFE_INTEGER,
     ]);
     expect(result.average).toBeDefined();
   });
   ```

## [Testing Guidelines]

1. Test Organization:

   ```javascript
   describe("UserManager", () => {
     describe("addUser", () => {
       test("success cases", () => {});
       test("validation cases", () => {});
       test("error cases", () => {});
     });

     describe("getUserStats", () => {
       test("calculation accuracy", () => {});
       test("empty database", () => {});
     });
   });
   ```

2. Mock Setup:

   ```javascript
   // Database mock
   const mockDb = {
     insert: jest.fn(),
     exists: jest.fn(),
     count: jest.fn(),
   };

   // Reset mocks between tests
   beforeEach(() => {
     jest.clearAllMocks();
   });
   ```

3. Assertion Best Practices:

   ```javascript
   // Be specific in assertions
   expect(result.username).toBe("john"); // Better than expect(result).toHaveProperty('username')

   // Test for exact error messages
   expect(() => {}).toThrow("Username already exists");

   // Check all relevant properties
   expect(result).toEqual({
     id: expect.any(Number),
     username: "john",
     email: "john@example.com",
     active: true,
   });
   ```

## [Practice Exercise]

1. Choose a class to test:

   - UserManager for async/database testing
   - DataProcessor for synchronous/pure function testing

2. Write test cases for:

   - Basic functionality
   - Input validation
   - Error handling
   - Edge cases
   - Performance considerations

3. Implement tests following these steps:

   - Set up test environment
   - Create mock objects
   - Write test cases
   - Run and verify tests
   - Measure coverage

4. Test Coverage Goals:
   - Line coverage: >90%
   - Branch coverage: >85%
   - Function coverage: 100%
   - Path coverage: >80%

## [Best Practices]

1. Follow the Arrange-Act-Assert pattern
2. Use descriptive test names
3. Test one thing per test function
4. Mock external dependencies
5. Keep tests independent
6. Write maintainable test code

## [Examples]

See `unit_testing.js` and `unit_testing.py` for practical examples of:

- Function unit tests
- Class unit tests
- Integration tests
- Mock object usage
- Test coverage analysis
