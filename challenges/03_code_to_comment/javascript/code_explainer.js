/**
 * Code Explainer Example
 * 
 * This file demonstrates GitHub Copilot's ability to help document code.
 * Each method contains complex algorithms that need documentation.
 * Use Copilot to help write detailed comments explaining what the code does.
 */

class TreeNode {
    constructor(value) {
        this.value = value;
        this.left = null;
        this.right = null;
    }
}

class TreeAnalysis {
    constructor(height, nodes, isBalanced, isBST) {
        this.height = height;
        this.nodes = nodes;
        this.isBalanced = isBalanced;
        this.isBST = isBST;
    }
}

class CodeExplainer {
    /**
     * TODO: Use GitHub Copilot to write detailed comments explaining this binary tree analysis algorithm.
     * Consider:
     * - What properties does it analyze?
     * - How does it determine if a tree is balanced?
     * - How does it verify BST properties?
     * - What are the edge cases?
     * - What is the time and space complexity?
     */
    static analyzeBinaryTree(root) {
        if (!root) {
            return new TreeAnalysis(0, 0, true, true);
        }

        const leftAnalysis = this.analyzeBinaryTree(root.left);
        const rightAnalysis = this.analyzeBinaryTree(root.right);

        const height = Math.max(leftAnalysis.height, rightAnalysis.height) + 1;
        const nodes = leftAnalysis.nodes + rightAnalysis.nodes + 1;
        const isBalanced = Math.abs(leftAnalysis.height - rightAnalysis.height) <= 1 
            && leftAnalysis.isBalanced && rightAnalysis.isBalanced;
        
        const isBST = leftAnalysis.isBST && rightAnalysis.isBST
            && (!root.left || this.findMax(root.left).value < root.value)
            && (!root.right || this.findMin(root.right).value > root.value);

        return new TreeAnalysis(height, nodes, isBalanced, isBST);
    }

    /**
     * TODO: Use GitHub Copilot to write detailed comments explaining this string pattern matching algorithm.
     * Consider:
     * - What algorithm is being implemented?
     * - How does the pattern table work?
     * - What are the key steps in the process?
     * - What are the edge cases?
     * - What is the time and space complexity?
     */
    static findPatternKMP(text, pattern) {
        if (!pattern || !text || pattern.length > text.length) {
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
     * TODO: Use GitHub Copilot to write detailed comments explaining this graph algorithm.
     * Consider:
     * - What algorithm is being implemented?
     * - How does it handle negative weights?
     * - What happens with negative cycles?
     * - What are the edge cases?
     * - What is the time and space complexity?
     */
    static floydWarshall(graph) {
        const V = graph.length;
        const dist = Array.from({ length: V }, () => 
            Array.from({ length: V }, () => Infinity)
        );

        for (let i = 0; i < V; i++) {
            for (let j = 0; j < V; j++) {
                dist[i][j] = graph[i][j];
            }
        }

        for (let k = 0; k < V; k++) {
            for (let i = 0; i < V; i++) {
                for (let j = 0; j < V; j++) {
                    if (dist[i][k] !== Infinity && dist[k][j] !== Infinity
                        && dist[i][k] + dist[k][j] < dist[i][j]) {
                        dist[i][j] = dist[i][k] + dist[k][j];
                    }
                }
            }
        }

        // Check for negative cycles
        for (let i = 0; i < V; i++) {
            if (dist[i][i] < 0) {
                throw new Error("Graph contains negative weight cycle");
            }
        }

        return dist;
    }

    static findMax(node) {
        while (node.right) {
            node = node.right;
        }
        return node;
    }

    static findMin(node) {
        while (node.left) {
            node = node.left;
        }
        return node;
    }
}

// Example usage
const root = new TreeNode(5);
root.left = new TreeNode(3);
root.right = new TreeNode(7);
root.left.left = new TreeNode(1);
root.left.right = new TreeNode(4);
root.right.left = new TreeNode(6);
root.right.right = new TreeNode(8);

console.log('Tree Analysis:', CodeExplainer.analyzeBinaryTree(root));
console.log('Pattern Matches:', CodeExplainer.findPatternKMP('AABAACAADAABAAABAA', 'AABA'));

const graph = [
    [0, 3, Infinity, 5],
    [2, 0, Infinity, 4],
    [Infinity, 1, 0, Infinity],
    [Infinity, Infinity, 2, 0]
];
console.log('Shortest Paths:', CodeExplainer.floydWarshall(graph));

// Practice exercises:
// TODO: Use GitHub Copilot to document these algorithms
// 1. Red-Black Tree operations
// 2. A* pathfinding algorithm
// 3. Quick Sort with different pivots
// 4. Topological sort
// 5. Minimum spanning tree

module.exports = CodeExplainer; 