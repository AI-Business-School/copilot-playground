/**
 * Code Documentation Example
 * 
 * This file demonstrates how to use GitHub Copilot for generating documentation from code.
 * Each section contains complex algorithms that need to be documented with clear explanations.
 */

class CodeDocumenter {
    /**
     * TODO: Ask Copilot to document this binary search tree analysis function.
     * Include:
     * - Purpose and overview of the algorithm
     * - Properties being analyzed (height, balance, BST validity)
     * - Time and space complexity
     * - Edge cases and error handling
     */
    static analyzeBinaryTree(root) {
        if (!root) {
            return {
                height: 0,
                nodes: 0,
                isBalanced: true,
                isBST: true
            };
        }

        const leftAnalysis = this.analyzeBinaryTree(root.left);
        const rightAnalysis = this.analyzeBinaryTree(root.right);

        const height = Math.max(leftAnalysis.height, rightAnalysis.height) + 1;
        const nodes = leftAnalysis.nodes + rightAnalysis.nodes + 1;
        const isBalanced = Math.abs(leftAnalysis.height - rightAnalysis.height) <= 1 &&
                          leftAnalysis.isBalanced && rightAnalysis.isBalanced;

        const isBST = leftAnalysis.isBST && rightAnalysis.isBST &&
                     (!root.left || this.findMax(root.left) < root.value) &&
                     (!root.right || this.findMin(root.right) > root.value);

        return { height, nodes, isBalanced, isBST };
    }

    /**
     * TODO: Ask Copilot to document this string pattern matching function.
     * Include:
     * - Purpose and overview of the KMP algorithm
     * - Pattern table construction and usage
     * - Time and space complexity
     * - Edge cases and error handling
     */
    static findPatternKMP(text, pattern) {
        if (!pattern || !text) {
            return [];
        }

        const lps = new Array(pattern.length).fill(0);
        let len = 0;
        let i = 1;

        while (i < pattern.length) {
            if (pattern[i] === pattern[len]) {
                len++;
                lps[i] = len;
                i++;
            } else {
                if (len !== 0) {
                    len = lps[len - 1];
                } else {
                    lps[i] = 0;
                    i++;
                }
            }
        }

        const matches = [];
        i = 0;
        let j = 0;

        while (i < text.length) {
            if (pattern[j] === text[i]) {
                i++;
                j++;
            }
            if (j === pattern.length) {
                matches.push(i - j);
                j = lps[j - 1];
            } else if (i < text.length && pattern[j] !== text[i]) {
                if (j !== 0) {
                    j = lps[j - 1];
                } else {
                    i++;
                }
            }
        }

        return matches;
    }

    /**
     * TODO: Ask Copilot to document this graph shortest paths function.
     * Include:
     * - Purpose and overview of the Floyd-Warshall algorithm
     * - Matrix representation and updates
     * - Time and space complexity
     * - Edge cases and error handling (negative cycles)
     */
    static floydWarshall(graph) {
        const n = graph.length;
        const dist = Array.from({ length: n }, (_, i) =>
            Array.from({ length: n }, (_, j) => graph[i][j])
        );

        for (let k = 0; k < n; k++) {
            for (let i = 0; i < n; i++) {
                for (let j = 0; j < n; j++) {
                    if (dist[i][k] !== Infinity && dist[k][j] !== Infinity) {
                        const newDist = dist[i][k] + dist[k][j];
                        if (newDist < dist[i][j]) {
                            dist[i][j] = newDist;
                        }
                    }
                }
            }
        }

        // Check for negative cycles
        for (let i = 0; i < n; i++) {
            if (dist[i][i] < 0) {
                throw new Error('Graph contains negative weight cycle');
            }
        }

        return dist;
    }

    // Helper functions
    static findMax(node) {
        while (node.right) {
            node = node.right;
        }
        return node.value;
    }

    static findMin(node) {
        while (node.left) {
            node = node.left;
        }
        return node.value;
    }
}

// Example usage
function runExamples() {
    // Test binary tree analysis
    const tree = {
        value: 10,
        left: {
            value: 5,
            left: { value: 3, left: null, right: null },
            right: { value: 7, left: null, right: null }
        },
        right: {
            value: 15,
            left: { value: 12, left: null, right: null },
            right: { value: 18, left: null, right: null }
        }
    };

    console.log('Binary Tree Analysis:', CodeDocumenter.analyzeBinaryTree(tree));

    // Test pattern matching
    const text = 'ABABDABACDABABCABAB';
    const pattern = 'ABABCABAB';
    console.log('Pattern Matches:', CodeDocumenter.findPatternKMP(text, pattern));

    // Test shortest paths
    const graph = [
        [0, 5, Infinity, 10],
        [Infinity, 0, 3, Infinity],
        [Infinity, Infinity, 0, 1],
        [Infinity, Infinity, Infinity, 0]
    ];

    console.log('Shortest Paths:', CodeDocumenter.floydWarshall(graph));
}

// Practice exercises:
// TODO: Ask Copilot to document these algorithms
// 1. Red-Black Tree operations
// 2. A* pathfinding algorithm
// 3. Topological sort
// 4. Network flow algorithms
// 5. Dynamic programming solutions

module.exports = CodeDocumenter; 