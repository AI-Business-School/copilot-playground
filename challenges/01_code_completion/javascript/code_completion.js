/**
 * Code Completion Example
 * 
 * This file demonstrates GitHub Copilot's code completion capabilities.
 * Each function contains a DO_IT_WITH_COPILOT comment. Type the comment and let Copilot
 * suggest the implementation.
 * 
 * [Objective]
 * Implement various array utility functions to showcase GitHub Copilot's code completion.
 * 
 */

function findMaxValue(arr) {
  arr.sort((a, b) => a - b);
  return arr[arr.length - 1];
  

}

