# This is a Python script to demonstrate advanced data structures using GitHub Copilot.

# Import necessary modules
from collections import deque
import heapq

# Function to demonstrate a deque (double-ended queue)
def deque_example():
    # Create a deque
    dq = deque()
    # Add elements to the deque
    dq.append(1)
    dq.append(2)
    dq.append(3)
    # Add elements to the left end of the deque
    dq.appendleft(0)
    # Remove elements from the deque
    dq.pop()
    dq.popleft()
    # Print the deque
    print("Deque:", dq)

# Function to demonstrate a heap (priority queue)
def heap_example():
    # Create a list of elements
    elements = [4, 1, 7, 3, 8, 5]
    # Convert the list to a heap
    heapq.heapify(elements)
    # Add elements to the heap
    heapq.heappush(elements, 2)
    heapq.heappush(elements, 6)
    # Remove the smallest element from the heap
    smallest = heapq.heappop(elements)
    # Print the heap and the smallest element
    print("Heap:", elements)
    print("Smallest element:", smallest)

# Function to demonstrate a trie (prefix tree)
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_of_word

    def starts_with(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True

# Example usage
deque_example()
heap_example()

trie = Trie()
trie.insert("hello")
trie.insert("world")
print("Search 'hello':", trie.search("hello"))
print("Search 'world':", trie.search("world"))
print("Search 'hell':", trie.search("hell"))
print("Starts with 'he':", trie.starts_with("he"))
print("Starts with 'wo':", trie.starts_with("wo"))
