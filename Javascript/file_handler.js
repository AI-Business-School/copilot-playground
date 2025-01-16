
// Exercise: File Handler
// Practice file operations with Github Copilot

const fs = require('fs').promises;

// TODO: Write a function that reads a file and counts the occurrences of each word
async function countWords(filename) {
    const data = await fs.readFile(filename, 'utf8');
    const words = data.split(/\s+/);
    const wordCount = {};
    words.forEach(word => {
        word = word.toLowerCase();
        wordCount[word] = (wordCount[word] || 0) + 1;
    });
    return wordCount;
}

// TODO: Write a function that writes a dictionary to a JSON file
async function writeToJson(data, filename) {
    const jsonData = JSON.stringify(data, null, 2);
    await fs.writeFile(filename, jsonData, 'utf8');
}

// TODO: Write a function that merges two text files
async function mergeFiles(file1, file2, outputFile) {
    const data1 = await fs.readFile(file1, 'utf8');
    const data2 = await fs.readFile(file2, 'utf8');
    const mergedData = data1 + '\n' + data2;
    await fs.writeFile(outputFile, mergedData, 'utf8');
}

module.exports = {
    countWords,
    writeToJson,
    mergeFiles
};