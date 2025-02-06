// Code to be tested
class UserManager {
    /**
     * @param {Object} database - Database connection
     */
    constructor(database) {
        this.db = database;
        this.activeUsers = new Set();
    }

    /**
     * Adds a new user to the system.
     * Write tests that:
     * - Verify successful user creation
     * - Handle duplicate usernames
     * - Validate email format
     * - Mock database interactions
     * @param {string} username - User's username
     * @param {string} email - User's email
     * @returns {Object} Created user object
     */
    async addUser(username, email) {
        if (!this._isValidEmail(email)) {
            throw new Error("Invalid email format");
        }

        if (await this._userExists(username)) {
            throw new Error("Username already exists");
        }

        const user = {
            username,
            email,
            createdAt: new Date(),
            active: true
        };

        const userId = await this.db.insert('users', user);
        user.id = userId;
        this.activeUsers.add(username);
        return user;
    }

    _isValidEmail(email) {
        return email.includes('@') && email.split('@')[1].includes('.');
    }

    async _userExists(username) {
        return await this.db.exists('users', { username });
    }

    /**
     * Calculates user statistics.
     * Write tests that:
     * - Verify correct statistics calculation
     * - Handle empty user database
     * - Test performance with large datasets
     * @returns {Object} User statistics
     */
    async getUserStats() {
        const totalUsers = await this.db.count('users');
        const activeUsers = this.activeUsers.size;
        return {
            totalUsers,
            activeUsers,
            inactiveUsers: totalUsers - activeUsers
        };
    }
}

class DataProcessor {
    /**
     * Processes a list of numbers and returns statistics.
     * Write tests that:
     * - Verify correct calculations
     * - Handle empty arrays
     * - Test with negative numbers
     * - Check for numerical precision
     * @param {number[]} numbers - Array of numbers to process
     * @returns {Object} Statistics object
     */
    processNumbers(numbers) {
        if (!numbers || numbers.length === 0) {
            throw new Error("Input array cannot be empty");
        }

        return {
            sum: numbers.reduce((a, b) => a + b, 0),
            average: numbers.reduce((a, b) => a + b, 0) / numbers.length,
            min: Math.min(...numbers),
            max: Math.max(...numbers)
        };
    }

    /**
     * Filters an array of objects based on given criteria.
     * Write tests that:
     * - Verify correct filtering
     * - Handle missing keys
     * - Test with empty input
     * - Check complex criteria
     * @param {Object[]} items - Array of objects to filter
     * @param {Object} criteria - Filter criteria
     * @returns {Object[]} Filtered array
     */
    filterData(items, criteria) {
        if (!items || !criteria || items.length === 0) {
            return [];
        }

        return items.filter(item => {
            return Object.entries(criteria).every(([key, value]) => 
                item.hasOwnProperty(key) && item[key] === value
            );
        });
    }
}

// Write your tests here using Jest
describe('UserManager', () => {
    // Write comprehensive unit tests for the UserManager class
});

describe('DataProcessor', () => {
    // Write comprehensive unit tests for the DataProcessor class
}); 