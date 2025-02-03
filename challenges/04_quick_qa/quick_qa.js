// Example 1: Code Explanation Question
/**
 * Q: What does this function do? How can it be improved?
 * @param {Array} items - Array of items to process
 * @returns {Object} - Processed result
 */
function processData(items) {
    const result = {};
    items.forEach(item => {
        result[item] = (result[item] || 0) + 1;
    });
    return result;
}

// Example 2: Debugging Question
/**
 * Q: Why might this function fail? What are the edge cases?
 * @param {Array<number>} numbers - Array of numbers
 * @returns {number} - Calculated average
 */
function calculateAverage(numbers) {
    const total = numbers.reduce((sum, num) => sum + num, 0);
    return total / numbers.length;
}

// Example 3: Performance Question
/**
 * Q: How can we optimize this function for better performance?
 * @param {Array} array - Input array to find duplicates in
 * @returns {Array} - Array of duplicate values
 */
function findDuplicates(array) {
    const duplicates = [];
    for (let i = 0; i < array.length; i++) {
        for (let j = i + 1; j < array.length; j++) {
            if (array[i] === array[j] && !duplicates.includes(array[i])) {
                duplicates.push(array[i]);
            }
        }
    }
    return duplicates;
}

// Example 4: Best Practices Question
/**
 * Q: How can we improve this class following JavaScript best practices?
 */
class DataProcessor {
    constructor() {
        this.data = [];
        this.processed = false;
    }

    addData(value) {
        this.data.push(value);
        this.processed = false;
    }

    process() {
        // Some processing logic here
        this.processed = true;
    }
} 