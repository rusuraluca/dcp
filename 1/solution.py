"""
Problem #1 [Easy]

This problem was recently asked by Google.

Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

Bonus: Can you do this in one pass?
"""

# One-pass solution using a set to track seen numbers.
# This solution checks for each number if its complement (k - num) has already been seen.
# Time complexity: O(n)
# Space complexity: O(n)
# where n is the number of elements in the list
def two_sum(nums, k):
    seen = set()
    for num in nums:
        if k - num in seen:
            return True
        seen.add(num)
    return False

# The current solution is optimal in terms of time complexity (O(n)) and space complexity (O(n)).
# A more space-efficient solution would involve sorting the list and using a two-pointer technique,
# but that would increase the time complexity to O(n log n) due to sorting.

# Tests:
def test_two_sum():
    assert two_sum([10, 15, 3, 7], 17) == True
    assert two_sum([10, 15, 3, 7], 100) == False
    assert two_sum([1, 2, 3, 4, 5], 9) == True
    assert two_sum([1, 2, 3, 4, 5], 10) == False
    assert two_sum([], 0) == False
    assert two_sum([5], 5) == False

# Example usage:
if __name__ == "__main__":
    test_two_sum()
    nums = [10, 15, 3, 7]
    k = 17
    print(two_sum(nums, k))  # Output: True
    k = 100
    print(two_sum(nums, k))  # Output: False
