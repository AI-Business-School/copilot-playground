
// Exercise: Array Operations
// Practice array manipulation tasks with Github Copilot

const numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];

// TODO: Write a function that finds all even numbers in the array
function findEvenNumbers(numbers) {
    return numbers.filter(number => number % 2 === 0);
}

// TODO: Write a function that calculates the average of all numbers
function calculateAverage(numbers) {
    const sum = numbers.reduce((acc, number) => acc + number, 0);
    return sum / numbers.length;
}

// TODO: Write a function that finds the largest and smallest numbers
function findMinMax(numbers) {
    const min = Math.min(...numbers);
    const max = Math.max(...numbers);
    return { min, max };
}

module.exports = {
    findEvenNumbers,
    calculateAverage,
    findMinMax
};