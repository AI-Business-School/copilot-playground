# Type Hinting Examples

This directory demonstrates GitHub Copilot's ability to help with type definitions through practical examples in both TypeScript and Python. The examples showcase how to use Copilot to generate and understand type hints, type safety, and advanced type features.

## Learning Objectives

1. Learn how to use GitHub Copilot to generate type definitions and type-safe code
2. Understand different type systems and their features in TypeScript and Python
3. Practice writing type-safe code with generics, protocols, and type guards
4. Explore advanced type features and type transformations

## Directory Structure

```
typescript/
└── type_helper.ts    # TypeScript implementation with type definitions
python/
└── type_helper.py    # Python implementation with type hints
```

## Examples

### Basic Types and Interfaces

```typescript
// TypeScript
interface User {
  id: string;
  name: string;
  email: string;
  role: "admin" | "user" | "guest";
  preferences?: UserPreferences;
}
```

```python
# Python
@dataclass
class User:
    id: UserId
    name: str
    email: str
    role: Role
    preferences: Optional[UserPreferences]
```

### Generic Types and Constraints

```typescript
// TypeScript
class Repository<T extends HasId> {
  async findById(id: string): Promise<T | undefined>;
  async create(item: Omit<T, "id">): Promise<T>;
}
```

```python
# Python
class Repository(Generic[T]):
    async def find_by_id(self, id: str) -> Optional[T]: ...
    async def create(self, item: Dict) -> T: ...
```

### Type Guards and Narrowing

```typescript
// TypeScript
function isUser(value: unknown): value is User {
  return (
    typeof value === "object" &&
    value !== null &&
    "id" in value &&
    "name" in value
  );
}
```

```python
# Python
def is_user(value: Any) -> TypeGuard[User]:
    return isinstance(value, dict) and 'id' in value and 'name' in value
```

## Challenges

1. Create a type-safe event system with typed event handlers
2. Implement a generic reducer with action types
3. Build a form validation system with typed fields
4. Design a type-safe API client
5. Create a dependency injection container with type safety

## Tips for Better Types

1. Start with interfaces and basic types
2. Use type constraints to enforce requirements
3. Leverage type inference when possible
4. Document complex type relationships
5. Consider performance implications

## What to Observe

1. How Copilot infers types from context
2. The way type constraints affect suggestions
3. Trade-offs between type safety and code complexity
4. Error messages and type checking
5. Type system differences between TypeScript and Python

## Learning Exercises

1. Write clear type definitions

   - Start with basic types
   - Add constraints
   - Document edge cases

2. Implement type guards

   - Handle unknown types
   - Narrow union types
   - Use type predicates

3. Explore advanced features

   - Mapped types
   - Conditional types
   - Template literal types

4. Practice type safety

   - Error handling
   - Null safety
   - Type assertions

5. Document type patterns
   - Type relationships
   - Generic constraints
   - Type composition

## Questions to Ask

1. Type Design

   - What types should this interface include?
   - How can we make this type more flexible?
   - Should we use a union or intersection type?

2. Generic Types

   - When should we use type parameters?
   - What constraints make sense here?
   - How can we improve type inference?

3. Type Safety

   - How can we prevent runtime errors?
   - What edge cases should we handle?
   - Is this type assertion safe?

4. Best Practices

   - What's the most maintainable approach?
   - How can we reduce type duplication?
   - Should we use type aliases or interfaces?

5. Implementation
   - How do we implement this type guard?
   - What's the best way to handle null values?
   - How can we make this code more type-safe?
