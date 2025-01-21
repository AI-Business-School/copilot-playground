/**
 * Type Hinting Example
 * 
 * This file demonstrates how to use GitHub Copilot for type hinting in JavaScript using JSDoc.
 * Each section contains types and protocols that you can ask questions about.
 */

// Basic Types using JSDoc
/**
 * @typedef {Object} UserPreferences
 * @property {string} theme - The user's preferred theme
 * @property {boolean} notifications - Whether notifications are enabled
 * @property {string} language - The user's preferred language
 */

/**
 * @typedef {Object} User
 * @property {string} id - Unique identifier
 * @property {string} name - User's full name
 * @property {string} email - User's email address
 * @property {'admin' | 'user' | 'guest'} role - User's role
 * @property {UserPreferences} [preferences] - Optional user preferences
 * @property {Date} createdAt - Account creation date
 * @property {Date} updatedAt - Last update date
 */

// Generic Types and Constraints using JSDoc
/**
 * @template T
 * Repository class for managing entities with IDs
 */
class Repository {
    /**
     * TODO: Ask Copilot questions about Repository implementation:
     * - How to handle type constraints?
     * - What about error handling?
     * - Should we use generics?
     * - How to implement caching?
     * - What about transaction support?
     */
    constructor(validate) {
        this.store = new Map();
        this.validate = validate;
    }

    /**
     * Find an entity by ID
     * @param {string} id - Entity ID
     * @returns {Promise<T | undefined>} Found entity or undefined
     */
    async findById(id) {
        return this.store.get(id);
    }

    /**
     * Find all entities
     * @returns {Promise<T[]>} Array of all entities
     */
    async findAll() {
        return Array.from(this.store.values());
    }

    /**
     * Create a new entity
     * @param {Omit<T, 'id'>} item - Entity data without ID
     * @returns {Promise<T>} Created entity
     * @throws {Error} If validation fails
     */
    async create(item) {
        const id = crypto.randomUUID();
        const newItem = { ...item, id };
        if (!this.validate(newItem)) {
            throw new Error('Invalid item');
        }
        this.store.set(id, newItem);
        return newItem;
    }

    /**
     * Update an existing entity
     * @param {string} id - Entity ID
     * @param {Partial<T>} item - Partial entity data
     * @returns {Promise<T>} Updated entity
     * @throws {Error} If entity not found or validation fails
     */
    async update(id, item) {
        const existing = this.store.get(id);
        if (!existing) {
            throw new Error('Item not found');
        }
        const updated = { ...existing, ...item };
        if (!this.validate(updated)) {
            throw new Error('Invalid item');
        }
        this.store.set(id, updated);
        return updated;
    }

    /**
     * Delete an entity
     * @param {string} id - Entity ID
     * @returns {Promise<boolean>} Whether the entity was deleted
     */
    async delete(id) {
        return this.store.delete(id);
    }
}

// Union Types and Type Guards using JSDoc
/**
 * @template T
 * @typedef {Object} Success
 * @property {true} success - Operation succeeded
 * @property {T} data - Result data
 */

/**
 * @typedef {Object} Failure
 * @property {false} success - Operation failed
 * @property {Error} error - Error information
 */

/**
 * @template T
 * @typedef {Success<T> | Failure} Result
 */

class TypeHelper {
    /**
     * TODO: Ask Copilot questions about Result handling:
     * - How to handle async operations?
     * - What about type inference?
     * - Should we use type guards?
     * - How to chain results?
     * - What about error types?
     * 
     * @template T
     * @param {() => Promise<T>} promise - Promise to handle
     * @returns {Promise<Result<T>>} Result object
     */
    static async handleResult(promise) {
        try {
            const data = await promise();
            return { success: true, data };
        } catch (error) {
            return { success: false, error };
        }
    }

    /**
     * TODO: Ask Copilot questions about type guards:
     * - When to use type predicates?
     * - How to narrow union types?
     * - What about branded types?
     * - Should we use assertions?
     * - How to handle unknown types?
     * 
     * @template T
     * @param {(value: unknown) => boolean} check - Type check function
     * @returns {(value: unknown) => value is T} Type guard function
     */
    static createTypeGuard(check) {
        return (value) => {
            try {
                return check(value);
            } catch {
                return false;
            }
        };
    }

    /**
     * TODO: Ask Copilot questions about type mapping:
     * - How to transform types?
     * - What about conditional types?
     * - Should we use template literals?
     * - How to handle recursion?
     * - What about type inference?
     * 
     * @template T,U
     * @param {(value: T) => U} transform - Transform function
     * @returns {(items: T[]) => U[]} Array transform function
     */
    static createTypeMapper(transform) {
        return (items) => items.map(transform);
    }
}

// Example usage
async function runExamples() {
    // Create a user repository
    const validateUser = (user) => {
        return (
            typeof user.id === 'string' &&
            typeof user.name === 'string' &&
            typeof user.email === 'string' &&
            ['admin', 'user', 'guest'].includes(user.role)
        );
    };

    const userRepo = new Repository(validateUser);

    // Test result handling
    const result = await TypeHelper.handleResult(() =>
        userRepo.create({
            name: 'Alice',
            email: 'alice@example.com',
            role: 'user',
            createdAt: new Date(),
            updatedAt: new Date()
        })
    );

    if (result.success) {
        console.log('Created user:', result.data);
    } else {
        console.log('Error:', result.error);
    }

    // Test type guard
    const isUser = TypeHelper.createTypeGuard((value) => {
        return (
            typeof value === 'object' &&
            value !== null &&
            'id' in value &&
            'name' in value &&
            'email' in value
        );
    });

    const unknownValue = { id: '1', name: 'Bob', email: 'bob@example.com' };
    if (isUser(unknownValue)) {
        console.log('Valid user:', unknownValue.name);
    }

    // Test type mapper
    const toUserDto = TypeHelper.createTypeMapper(
        user => ({ name: user.name, email: user.email })
    );

    const users = await userRepo.findAll();
    const dtos = toUserDto(users);
    console.log('User DTOs:', dtos);
}

// Practice exercises:
// TODO: Ask Copilot questions about these patterns
// 1. JSDoc type definitions
// 2. Type checking functions
// 3. Method overloading with JSDoc
// 4. Generic functions
// 5. Type assertions

module.exports = { Repository, TypeHelper }; 