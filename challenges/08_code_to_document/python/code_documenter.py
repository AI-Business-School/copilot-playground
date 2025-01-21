"""
Code Documentation Example

This file demonstrates how to use GitHub Copilot for generating documentation from code.
Each section contains complex algorithms that need to be documented with clear explanations.
"""

from typing import Optional, List, Dict, Union
from dataclasses import dataclass


@dataclass
class TreeNode:
    value: int
    left: Optional['TreeNode'] = None
    right: Optional['TreeNode'] = None


@dataclass
class TreeAnalysis:
    height: int
    nodes: int
    is_balanced: bool
    is_bst: bool


class CodeDocumenter:
    """
    TODO: Ask Copilot to document this class.
    Include:
    - Purpose and overview of the class
    - Description of each algorithm
    - Common use cases and examples
    """

    @staticmethod
    def analyze_binary_tree(root: Optional[TreeNode]) -> TreeAnalysis:
        """
        TODO: Ask Copilot to document this binary search tree analysis function.
        Include:
        - Purpose and overview of the algorithm
        - Properties being analyzed (height, balance, BST validity)
        - Time and space complexity
        - Edge cases and error handling
        """
        if not root:
            return TreeAnalysis(
                height=0,
                nodes=0,
                is_balanced=True,
                is_bst=True
            )

        left_analysis = CodeDocumenter.analyze_binary_tree(root.left)
        right_analysis = CodeDocumenter.analyze_binary_tree(root.right)

        height = max(left_analysis.height, right_analysis.height) + 1
        nodes = left_analysis.nodes + right_analysis.nodes + 1
        is_balanced = (abs(left_analysis.height - right_analysis.height) <= 1 and
                      left_analysis.is_balanced and right_analysis.is_balanced)

        is_bst = (left_analysis.is_bst and right_analysis.is_bst and
                 (not root.left or CodeDocumenter.find_max(root.left) < root.value) and
                 (not root.right or CodeDocumenter.find_min(root.right) > root.value))

        return TreeAnalysis(height=height, nodes=nodes, is_balanced=is_balanced, is_bst=is_bst)

    @staticmethod
    def find_pattern_kmp(text: str, pattern: str) -> List[int]:
        """
        TODO: Ask Copilot to document this string pattern matching function.
        Include:
        - Purpose and overview of the KMP algorithm
        - Pattern table construction and usage
        - Time and space complexity
        - Edge cases and error handling
        """
        if not pattern or not text:
            return []

        lps = [0] * len(pattern)
        length = 0
        i = 1

        while i < len(pattern):
            if pattern[i] == pattern[length]:
                length += 1
                lps[i] = length
                i += 1
            else:
                if length != 0:
                    length = lps[length - 1]
                else:
                    lps[i] = 0
                    i += 1

        matches = []
        i = 0
        j = 0

        while i < len(text):
            if pattern[j] == text[i]:
                i += 1
                j += 1
            if j == len(pattern):
                matches.append(i - j)
                j = lps[j - 1]
            elif i < len(text) and pattern[j] != text[i]:
                if j != 0:
                    j = lps[j - 1]
                else:
                    i += 1

        return matches

    @staticmethod
    def floyd_warshall(graph: List[List[float]]) -> List[List[float]]:
        """
        TODO: Ask Copilot to document this graph shortest paths function.
        Include:
        - Purpose and overview of the Floyd-Warshall algorithm
        - Matrix representation and updates
        - Time and space complexity
        - Edge cases and error handling (negative cycles)
        """
        n = len(graph)
        dist = [[graph[i][j] for j in range(n)] for i in range(n)]

        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if dist[i][k] != float('inf') and dist[k][j] != float('inf'):
                        new_dist = dist[i][k] + dist[k][j]
                        if new_dist < dist[i][j]:
                            dist[i][j] = new_dist

        # Check for negative cycles
        for i in range(n):
            if dist[i][i] < 0:
                raise ValueError('Graph contains negative weight cycle')

        return dist

    @staticmethod
    def find_max(node: TreeNode) -> int:
        """Helper function to find the maximum value in a binary tree."""
        while node.right:
            node = node.right
        return node.value

    @staticmethod
    def find_min(node: TreeNode) -> int:
        """Helper function to find the minimum value in a binary tree."""
        while node.left:
            node = node.left
        return node.value


def run_examples():
    """Run example cases for the CodeDocumenter class."""
    # Test binary tree analysis
    tree = TreeNode(
        value=10,
        left=TreeNode(
            value=5,
            left=TreeNode(value=3),
            right=TreeNode(value=7)
        ),
        right=TreeNode(
            value=15,
            left=TreeNode(value=12),
            right=TreeNode(value=18)
        )
    )

    print('Binary Tree Analysis:', CodeDocumenter.analyze_binary_tree(tree))

    # Test pattern matching
    text = 'ABABDABACDABABCABAB'
    pattern = 'ABABCABAB'
    print('Pattern Matches:', CodeDocumenter.find_pattern_kmp(text, pattern))

    # Test shortest paths
    graph = [
        [0, 5, float('inf'), 10],
        [float('inf'), 0, 3, float('inf')],
        [float('inf'), float('inf'), 0, 1],
        [float('inf'), float('inf'), float('inf'), 0]
    ]

    print('Shortest Paths:', CodeDocumenter.floyd_warshall(graph))


if __name__ == '__main__':
    run_examples()

# Practice exercises:
# TODO: Ask Copilot to document these algorithms
# 1. Red-Black Tree operations
# 2. A* pathfinding algorithm
# 3. Topological sort
# 4. Network flow algorithms
# 5. Dynamic programming solutions 