/**
 * Array Utilities Example
 * 
 * This file demonstrates GitHub Copilot's code completion capabilities.
 * Each method contains a TODO comment. Type the comment and let Copilot
 * suggest the implementation.
 */

class ArrayUtils {
    /**
     * TODO: Use GitHub Copilot to implement a method that finds the maximum value in an array.
     * Start typing the method signature and let Copilot complete it.
     * Try variations like:
     * - Handle empty arrays
     * - Support both numbers and comparable objects
     * - Add type checking
     */
    static findMax(arr) {
        // Your implementation here
    }

    /**
     * TODO: Use GitHub Copilot to implement a method that calculates the average of numbers.
     * Start typing the method signature and let Copilot complete it.
     * Try variations like:
     * - Handle empty arrays
     * - Filter out non-numeric values
     * - Support weighted averages
     */
    static calculateAverage(arr) {
        // Your implementation here
    }

    /**
     * TODO: Use GitHub Copilot to implement a method that removes duplicate elements.
     * Start typing the method signature and let Copilot complete it.
     * Try variations like:
     * - Preserve original order
     * - Custom equality comparison
     * - Handle nested objects
     */
    static removeDuplicates(arr) {
        // Your implementation here
    }

    /**
     * TODO: Use GitHub Copilot to implement a method that finds all prime numbers up to n.
     * Start typing the method signature and let Copilot complete it.
     * Try variations like:
     * - Optimize for large numbers
     * - Return prime factors
     * - Check primality
     */
    static findPrimes(n) {
        // Your implementation here
    }

    /**
     * TODO: Use GitHub Copilot to implement a method that rotates an array by k positions.
     * Start typing the method signature and let Copilot complete it.
     * Try variations like:
     * - Handle negative rotations
     * - In-place rotation
     * - Multiple array types
     */
    static rotateArray(arr, k) {
        // Your implementation here
    }

    /**
     * TODO: Use GitHub Copilot to implement a method that finds pairs summing to a target.
     * Start typing the method signature and let Copilot complete it.
     * Try variations like:
     * - Handle duplicates
     * - Return indices
     * - Find all possible pairs
     */
    static findPairs(arr, target) {
        // Your implementation here
    }
}

function runExamples() {
    // TODO: Use GitHub Copilot to generate test cases
    // Start typing test scenarios and let Copilot complete them
    const numbers = [4, 2, 7, 1, 9, 5];
    console.log('Max:', ArrayUtils.findMax(numbers));
    console.log('Average:', ArrayUtils.calculateAverage(numbers));
    console.log('No duplicates:', ArrayUtils.removeDuplicates([1, 2, 2, 3, 3, 4]));
    console.log('Primes up to 20:', ArrayUtils.findPrimes(20));
    console.log('Rotated array:', ArrayUtils.rotateArray([1, 2, 3, 4, 5], 2));
    console.log('Pairs summing to 10:', ArrayUtils.findPairs([2, 4, 6, 8, 3, 7], 10));
}

runExamples();

// Practice exercises:
// TODO: Use GitHub Copilot to implement these additional array operations
// 1. Merge two sorted arrays
// 2. Find the longest increasing subsequence
// 3. Implement a sliding window maximum
// 4. Create a circular buffer
// 5. Implement array chunking

module.exports = ArrayUtils; 