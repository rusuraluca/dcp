"""
Problem #3 [Medium]

This problem was asked by Google.

Given the root to a binary tree, implement serialize(root),
which serializes the tree into a string, and deserialize(s),
which deserializes the string back into the tree.

For example, given the following Node class

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

The following test should pass:

node = Node('root', Node('left', Node('left.left')), Node('right'))
assert deserialize(serialize(node)).left.left.val == 'left.left'
"""
# We can use pre-order traversal to serialize the tree.
# We will represent null nodes with a special marker (e.g., '#').
# During deserialization, we will use a queue to reconstruct the tree
# by reading values in the same order they were written during serialization.
# Time complexity of O(n)
# Space complexity of O(n)
# where n is the number of nodes in the binary tree.
from typing import Optional
from collections import deque


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def serialize(root: Optional['Node']) -> str:
    def helper(node):
        if node is None:
            result.append('#')
            return
        result.append(str(node.val))
        helper(node.left)
        helper(node.right)

    result = []
    helper(root)
    return ','.join(result)

def deserialize(data: str) -> Optional['Node']:
    def helper():
        val = next(values)
        if val == '#':
            return None
        node = Node(val)
        node.left = helper()
        node.right = helper()
        return node

    values = iter(data.split(','))
    return helper()

# Tests:
def test_serialize_deserialize():
    node = Node('root', Node('left', Node('left.left')), Node('right'))
    serialized = serialize(node)
    deserialized = deserialize(serialized)
    assert deserialized.left.left.val == 'left.left'
    assert deserialized.left.val == 'left'
    assert deserialized.right.val == 'right'
    assert deserialized.val == 'root'
    assert serialize(deserialized) == serialized
    print("All tests passed.")

# Example usage:
if __name__ == "__main__":
    test_serialize_deserialize() # Run tests
    node = Node('root', Node('left', Node('left.left')), Node('right'))
    serialized = serialize(node)
    print(f"Serialized: {serialized}") # Output: Serialized: root,left,left.left,#,#,#,right,#,#
    deserialized = deserialize(serialized)
    print(f"Deserialized left.left value: {deserialized.left.left.val}") # Output: Deserialized left.left value: left.left