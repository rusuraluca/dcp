"""
Problem #8 [Easy]

This problem was asked by Google.

A unival tree (which stands for "universal value") is a tree where all nodes under it have the same value.

Given the root to a binary tree, count the number of unival subtrees.

For example, the following tree has 5 unival subtrees:

   0
  / \
 1   0
    / \
   1   0
  / \
 1   1
"""
# We can solve this problem using a recursive approach.
# We will define a helper function that checks if a subtree is unival and counts the number
# of unival subtrees. The base case will be when we reach a null node,
# which is considered a unival subtree. For each node, we will check if its left and right
# subtrees are unival and if they have the same value as the current node.
# If they do, we will increment our count of unival subtrees.
# Time complexity of O(n)
# Space complexity of O(h)
# where n is the number of nodes in the tree and h is the height of the tree
from typing import Optional, Tuple


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def count_unival_subtrees(root: Optional['Node']) -> int:
    def helper(node: Optional['Node']) -> Tuple[bool, int]:
        if node is None:
            return True, 0  # A null node is a unival subtree

        left_is_unival, left_count = helper(node.left)
        right_is_unival, right_count = helper(node.right)

        total_count = left_count + right_count

        if left_is_unival and right_is_unival:
            if (node.left is None or node.left.val == node.val) and (node.right is None or node.right.val == node.val):
                return True, total_count + 1  # Current node is a unival subtree

        return False, total_count  # Current node is not a unival subtree

    _, count = helper(root)
    return count

# Tests:
def test_count_unival_subtrees():
    tree1 = Node(0, Node(1), Node(0, Node(1, Node(1), Node(1)), Node(0)))
    assert count_unival_subtrees(tree1) == 5

    tree2 = Node(1, Node(1), Node(1))
    assert count_unival_subtrees(tree2) == 3

    tree3 = Node(1, Node(2), Node(3))
    assert count_unival_subtrees(tree3) == 2

    tree4 = None
    assert count_unival_subtrees(tree4) == 0

    tree5 = Node(1)
    assert count_unival_subtrees(tree5) == 1

    tree6 = Node(1, Node(1, Node(1)), Node(1, Node(1)))
    assert count_unival_subtrees(tree6) == 5

    print("All tests passed.")

# Example usage:
if __name__ == "__main__":
    test_count_unival_subtrees() # Run tests
    tree = Node(0, Node(1), Node(0, Node(1, Node(1), Node(1)), Node(0)))
    print(count_unival_subtrees(tree)) # Output: 5
    tree = Node(1, Node(1), Node(1))
    print(count_unival_subtrees(tree)) # Output: 3
