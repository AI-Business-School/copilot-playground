"""
Code Explainer Example

This file demonstrates GitHub Copilot's ability to help document code.
Each method contains complex algorithms that need documentation.
Use Copilot to help write detailed comments explaining what the code does.
"""

from typing import List, Optional, Dict, Any, Union
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

class CodeExplainer:
    """Collection of algorithms that need documentation"""

    @staticmethod
    def analyze_binary_tree(root: Optional[TreeNode]) -> TreeAnalysis:
        """
        TODO: Use GitHub Copilot to write detailed comments explaining this binary tree analysis algorithm.
        Consider:
        - What properties does it analyze?
        - How does it determine if a tree is balanced?
        - How does it verify BST properties?
        - What are the edge cases?
        - What is the time and space complexity?
        """
        if not root:
            return TreeAnalysis(0, 0, True, True)

        left_analysis = CodeExplainer.analyze_binary_tree(root.left)
        right_analysis = CodeExplainer.analyze_binary_tree(root.right)

        height = max(left_analysis.height, right_analysis.height) + 1
        nodes = left_analysis.nodes + right_analysis.nodes + 1
        is_balanced = abs(left_analysis.height - right_analysis.height) <= 1 \
            and left_analysis.is_balanced and right_analysis.is_balanced
        
        is_bst = left_analysis.is_bst and right_analysis.is_bst \
            and (not root.left or CodeExplainer.find_max(root.left).value < root.value) \
            and (not root.right or CodeExplainer.find_min(root.right).value > root.value)

        return TreeAnalysis(height, nodes, is_balanced, is_bst)

    @staticmethod
    def find_pattern_kmp(text: str, pattern: str) -> List[int]:
        """
        TODO: Use GitHub Copilot to write detailed comments explaining this string pattern matching algorithm.
        Consider:
        - What algorithm is being implemented?
        - How does the pattern table work?
        - What are the key steps in the process?
        - What are the edge cases?
        - What is the time and space complexity?
        """
        if not pattern or not text or len(pattern) > len(text):
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
        TODO: Use GitHub Copilot to write detailed comments explaining this graph algorithm.
        Consider:
        - What algorithm is being implemented?
        - How does it handle negative weights?
        - What happens with negative cycles?
        - What are the edge cases?
        - What is the time and space complexity?
        """
        V = len(graph)
        dist = [[float('inf')] * V for _ in range(V)]

        for i in range(V):
            for j in range(V):
                dist[i][j] = graph[i][j]

        for k in range(V):
            for i in range(V):
                for j in range(V):
                    if dist[i][k] != float('inf') and dist[k][j] != float('inf') \
                        and dist[i][k] + dist[k][j] < dist[i][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]

        # Check for negative cycles
        for i in range(V):
            if dist[i][i] < 0:
                raise ValueError("Graph contains negative weight cycle")

        return dist

    @staticmethod
    def find_max(node: TreeNode) -> TreeNode:
        while node.right:
            node = node.right
        return node

    @staticmethod
    def find_min(node: TreeNode) -> TreeNode:
        while node.left:
            node = node.left
        return node

def run_examples():
    """Example usage of the algorithms"""
    # Create a binary search tree
    root = TreeNode(5)
    root.left = TreeNode(3)
    root.right = TreeNode(7)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(4)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(8)

    # Test tree analysis
    print('Tree Analysis:', CodeExplainer.analyze_binary_tree(root))

    # Test pattern matching
    print('Pattern Matches:', CodeExplainer.find_pattern_kmp('AABAACAADAABAAABAA', 'AABA'))

    # Test shortest paths
    graph = [
        [0, 3, float('inf'), 5],
        [2, 0, float('inf'), 4],
        [float('inf'), 1, 0, float('inf')],
        [float('inf'), float('inf'), 2, 0]
    ]
    print('Shortest Paths:', CodeExplainer.floyd_warshall(graph))

if __name__ == "__main__":
    run_examples()

# Practice exercises:
# TODO: Use GitHub Copilot to document these algorithms
# 1. Red-Black Tree operations
# 2. A* pathfinding algorithm
# 3. Quick Sort with different pivots
# 4. Topological sort
# 5. Minimum spanning tree 