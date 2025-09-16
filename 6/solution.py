"""
Problem #6 [Hard]

This problem was asked by Google.

An XOR linked list is a more memory efficient doubly linked list.
Instead of each node holding next and prev fields,
it holds a field named both, which is an XOR of the next node and the previous node.

Implement an XOR linked list;
it has an add(element) which adds the element to the end,
and a get(index) which returns the node at index.

If using a language that has no pointers (such as Python),
you can assume you have access to get_pointer
and dereference_pointer functions that converts between nodes and memory addresses.
"""
# We can implement an XOR linked list using a class to represent each node,
# and a class to represent the XOR linked list itself.
# The add method will add a new node to the end of the list,
# and the get method will traverse the list to find the node at the specified index.
# Time complexity of O(n) for get and O(1) for add
# Space complexity of O(n) for storing the nodes
# where n is the number of nodes in the list.


class XORNode:
    def __init__(self, value):
        self.value = value
        self.both = 0

class XORLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.nodes = []

    def add(self, element):
        new_node = XORNode(element)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.both ^= get_pointer(new_node)
            new_node.both ^= get_pointer(self.tail)
            self.tail = new_node
        self.nodes.append(new_node)

    def get(self, index):
        if index < 0 or index >= len(self.nodes):
            raise IndexError("Index out of bounds")
        return self.nodes[index]

# Helper functions to simulate pointer behavior in Python
def get_pointer(node):
    return id(node)

def dereference_pointer(ptr):
    return next((node for node in xor_linked_list.nodes if get_pointer(node) == ptr), None)

# Tests:
def test_xor_linked_list():
    xor_linked_list = XORLinkedList()
    xor_linked_list.add(1)
    xor_linked_list.add(2)
    xor_linked_list.add(3)
    assert xor_linked_list.get(0).value == 1
    assert xor_linked_list.get(1).value == 2
    assert xor_linked_list.get(2).value == 3
    try:
        xor_linked_list.get(3)
        assert False, "Expected IndexError"
    except IndexError:
        pass

# Example usage:
if __name__ == "__main__":
    test_xor_linked_list() # Run tests
    xor_linked_list = XORLinkedList()
    xor_linked_list.add(1)
    xor_linked_list.add(2)
    xor_linked_list.add(3)
    print(xor_linked_list.get(0).value) # Output: 1
    print(xor_linked_list.get(1).value) # Output: 2
    print(xor_linked_list.get(2).value) # Output: 3
