"""
Problem #9 [Hard]

This problem was asked by Airbnb.

Given a list of integers, write a function that returns the largest sum of non-adjacent numbers. Numbers can be 0 or negative.

For example, [2, 4, 6, 2, 5] should return 13, since we pick 2, 6, and 5. [5, 1, 1, 5] should return 10, since we pick 5 and 5.

Follow-up: Can you do this in O(N) time and constant space?
"""
# We can solve this problem using dynamic programming.
# The idea is to maintain two variables, `incl` and `excl`.
# `incl` will store the maximum sum including the current element,
# and `excl` will store the maximum sum excluding the current element.
# For each element in the list, we update `incl` to be the sum of `excl` and the current element,
# and `excl` to be the maximum of the previous `incl` and `excl`.
# This way, we ensure that no two adjacent elements are included in the sum.
# Time complexity of O(n)
# Space complexity of O(1)
# where n is the number of elements in the input list.
from typing import List


def largest_non_adjacent_sum(arr: List[int]) -> int:
    if not arr:
        return 0

    incl = 0  # Max sum including the previous element
    excl = 0  # Max sum excluding the previous element

    for num in arr:
        # Current max excluding i (no adjacent)
        new_excl = max(incl, excl)

        # Current max including i
        incl = excl + num
        excl = new_excl

    return max(incl, excl)

# Tests:
def test_largest_non_adjacent_sum():
    assert largest_non_adjacent_sum([2, 4, 6, 2, 5]) == 13
    assert largest_non_adjacent_sum([5, 1, 1, 5]) == 10
    assert largest_non_adjacent_sum([-1, -2, -3]) == 0
    assert largest_non_adjacent_sum([3, 2, 5, 10, 7]) == 15
    assert largest_non_adjacent_sum([]) == 0
    assert largest_non_adjacent_sum([1]) == 1
    assert largest_non_adjacent_sum([1, 2]) == 2
    assert largest_non_adjacent_sum([2, 1]) == 2
    assert largest_non_adjacent_sum([1, -1, 3, -2, 5]) == 8
    assert largest_non_adjacent_sum([-1, 2, -3, 4, -5, 6]) == 12
    print("All tests passed.")

# Example usage:
if __name__ == "__main__":
    test_largest_non_adjacent_sum()  # Run tests
    arr = [2, 4, 6, 2, 5]
    print(largest_non_adjacent_sum(arr))  # Output: 13
    arr = [5, 1, 1, 5]
    print(largest_non_adjacent_sum(arr))  # Output: 10
