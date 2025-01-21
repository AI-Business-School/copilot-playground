/**
 * Data Transformer Example
 * 
 * This file demonstrates GitHub Copilot's ability to generate code from comments.
 * Each method contains a detailed comment describing what the code should do.
 * Type the comment and let Copilot generate the implementation.
 */

class DataTransformer {
    /**
     * TODO: Let GitHub Copilot implement a method that transforms an array of user objects 
     * into a map where keys are user IDs and values are user objects.
     * 
     * Requirements:
     * - If a user has no ID, use array index as fallback
     * - Handle duplicate IDs by keeping the last occurrence
     * - Skip null/undefined users
     * - Preserve all other user properties
     * 
     * Example input:
     * [
     *   { id: 2, name: 'Jane', role: 'admin' },
     *   { name: 'John', role: 'user' },
     *   { id: 1, name: 'Mike', role: 'user' }
     * ]
     * 
     * Example output:
     * {
     *   '1': { id: 1, name: 'Mike', role: 'user' },
     *   '2': { id: 2, name: 'Jane', role: 'admin' },
     *   '3': { name: 'John', role: 'user' }
     * }
     */
    static arrayToMap(users) {
        // Your implementation here
    }

    /**
     * TODO: Let GitHub Copilot implement a method that converts a nested object 
     * into a flat object where keys are dot-separated paths.
     * 
     * Requirements:
     * - Handle nested objects of any depth
     * - Convert array indices to numeric path segments
     * - Skip undefined/null values
     * - Preserve primitive values
     * 
     * Example input:
     * {
     *   user: {
     *     name: 'John',
     *     address: {
     *       city: 'NY',
     *       coords: [40.7, -73.9]
     *     }
     *   },
     *   active: true
     * }
     * 
     * Example output:
     * {
     *   'user.name': 'John',
     *   'user.address.city': 'NY',
     *   'user.address.coords.0': 40.7,
     *   'user.address.coords.1': -73.9,
     *   'active': true
     * }
     */
    static flattenObject(obj, prefix = '') {
        // Your implementation here
    }

    /**
     * TODO: Let GitHub Copilot implement a method that groups an array of items 
     * by multiple keys, creating a nested structure.
     * 
     * Requirements:
     * - Support an array of key names for grouping
     * - Create nested groups based on key order
     * - Use 'unknown' for missing values
     * - Preserve original items in leaf nodes
     * 
     * Example input:
     * Items: [
     *   { dept: 'tech', role: 'dev', name: 'John' },
     *   { dept: 'tech', role: 'dev', name: 'Jane' },
     *   { dept: 'sales', name: 'Mike' }
     * ]
     * Keys: ['dept', 'role']
     * 
     * Example output:
     * {
     *   'tech': {
     *     'dev': [
     *       { dept: 'tech', role: 'dev', name: 'John' },
     *       { dept: 'tech', role: 'dev', name: 'Jane' }
     *     ]
     *   },
     *   'sales': {
     *     'unknown': [
     *       { dept: 'sales', name: 'Mike' }
     *     ]
     *   }
     * }
     */
    static groupByMultipleKeys(items, keys) {
        // Your implementation here
    }
}

// Example usage
const users = [
    { id: 2, name: 'Jane', role: 'admin' },
    { name: 'John', role: 'user' },
    { id: 1, name: 'Mike', role: 'user' }
];

const nested = {
    user: {
        name: 'John',
        address: {
            city: 'NY',
            coords: [40.7, -73.9]
        }
    },
    active: true
};

const items = [
    { dept: 'tech', role: 'dev', name: 'John' },
    { dept: 'tech', role: 'dev', name: 'Jane' },
    { dept: 'sales', name: 'Mike' }
];

console.log('Users map:', DataTransformer.arrayToMap(users));
console.log('Flattened object:', DataTransformer.flattenObject(nested));
console.log('Grouped items:', DataTransformer.groupByMultipleKeys(items, ['dept', 'role']));

// Practice exercises:
// TODO: Use GitHub Copilot to implement these additional transformations
// 1. Transform snake_case keys to camelCase
// 2. Convert array of arrays to CSV string
// 3. Create a deep clone function
// 4. Build a query string from object
// 5. Transform XML to JSON

module.exports = DataTransformer; 