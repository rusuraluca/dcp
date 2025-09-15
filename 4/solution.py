"""
Problem #4 [Hard]

This problem was asked by Stripe.

Given an array of integers,
find the first missing positive integer in linear time and constant space.
In other words, find the lowest positive integer that does not exist in the array.
The array can contain duplicates and negative numbers as well.

For example, the input [3, 4, -1, 1] should give 2.
The input [1, 2, 0] should give 3.

You can modify the input array in-place.
"""
# We can solve this problem by using the input array itself to track
# which positive integers are present. The idea is to place each positive integer n at index n
# (i.e., 1 at index 0, 2 at index 1, etc.). We will iterate through the array and for each
# positive integer that is within the range of the array (1 to len(arr)), we will
# swap it to its correct position. After this rearrangement, we will iterate through the
# array again to find the first index that does not contain the correct integer.
# Time complexity of O(n)
# Space complexity of O(1)
# where n is the number of elements in the input array.
from typing import List


def first_missing_positive(arr: List[int]) -> int:
    n = len(arr)

    # Step 1: Place each number in its right place, e.g., 1 at index 0, 2 at index 1, etc.
    for i in range(n):
        while 1 <= arr[i] <= n and arr[arr[i] - 1] != arr[i]:
            # Swap arr[i] with arr[arr[i] - 1]
            correct_index = arr[i] - 1
            arr[i], arr[correct_index] = arr[correct_index], arr[i]

    # Step 2: Find the first index that does not have the correct integer
    for i in range(n):
        if arr[i] != i + 1:
            return i + 1

    # If all indices have the correct integers, return n + 1
    return n + 1

# Tests:
def test_first_missing_positive():
    assert first_missing_positive([3, 4, -1, 1]) == 2
    assert first_missing_positive([1, 2, 0]) == 3
    assert first_missing_positive([7, 8, 9, 11, 12]) == 1
    assert first_missing_positive([1, 2, 3]) == 4
    assert first_missing_positive([-1, -2, -3]) == 1
    assert first_missing_positive([2, 2, 2, 2]) == 1
    assert first_missing_positive([]) == 1
    assert first_missing_positive([1]) == 2
    assert first_missing_positive([2]) == 1
    assert first_missing_positive([1, 1]) == 2
    assert first_missing_positive([2, 1]) == 3
    assert first_missing_positive([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 11
    assert first_missing_positive([10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 11
    print("All tests passed.")

# Example usage:
if __name__ == "__main__":
    test_first_missing_positive() # Run tests
    arr = [3, 4, -1, 1]
    print(first_missing_positive(arr)) # Output: 2
    arr = [1, 2, 0]
    print(first_missing_positive(arr)) # Output: 3
