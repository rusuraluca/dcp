"""
Problem #2 [Hard]

This problem was asked by Uber.

Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].

Follow-up: what if you can't use division?
"""

# We can calculate the total product of all elements
# and then for each element in the array, divide the total product by that element to get
# the product of all other elements. However, this approach fails if any element is zero.

# Two-pass solution by computing prefix and suffix products,
# multiplying them to get the final result.
# We maintain two pointers, one for the prefix product and one for the suffix product.
# We iterate through the array twice: once from left to right to compute the prefix products,
# and once from right to left to compute the suffix products.
# This way, each position in the output array contains the product of all elements except the one at that position.
# Time complexity of O(n)
# Space complexity of O(n)
# where n is the number of elements in the input array.
from typing import List

def product_array(arr: List[int]) -> List[int]:
    n = len(arr)
    if n == 0:
        return []

    # Initialize the output array with 1s
    output = [1] * n

    # Calculate the prefix products
    prefix_product = 1
    for i in range(n):
        output[i] = prefix_product
        prefix_product *= arr[i]

    # Calculate the suffix products and multiply with the prefix products
    suffix_product = 1
    for i in range(n - 1, -1, -1):
        output[i] *= suffix_product
        suffix_product *= arr[i]

    return output

# A more space-efficient solution would involve using the output array to store intermediate
# results, but that would still require O(n) space for the output itself.

# Tests:
def test_product_array():
    assert product_array([1, 2, 3, 4, 5]) == [120, 60, 40, 30, 24]
    assert product_array([3, 2, 1]) == [2, 3, 6]
    assert product_array([0, 1, 2]) == [2, 0, 0]
    assert product_array([1, -1, 1]) == [-1, 1, -1]
    assert product_array([]) == []
    assert product_array([5]) == [1]
    print("All tests passed.")

# Example usage:
if __name__ == "__main__":
    test_product_array() # Run tests
    arr = [1, 2, 3, 4, 5]
    print(product_array(arr))  # Output: [120, 60, 40, 30, 24]
    arr = [3, 2, 1]
    print(product_array(arr))  # Output: [2, 3, 6]
