// Example 1: Simple function with array input
// Function name: calculateAverage
// Input: numbers (array of numbers)
// Output: number (average of the array)
function calculateAverage(numbers) {
    const sum = numbers.reduce((a, b) => a + b, 0);
    return sum / numbers.length;
}

// Example 2: String manipulation
// Function name: reverseAndCapitalize
// Input: text (string)
// Output: reversed and capitalized string
function reverseAndCapitalize(text) {
    return text.split('').reverse().join('').toUpperCase();
}

// Example 3: Object transformation
// Function name: formatPerson
// Input: person (object with name and age)
// Output: formatted string
function formatPerson(person) {
    return `${person.name} is ${person.age} years old`;
}
