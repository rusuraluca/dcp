"""
Problem #12 [Hard]
This problem was asked by Amazon.

There exists a staircase with N steps, and you can climb up either 1 or 2 steps at a time.
Given N, write a function that returns the number of unique ways you can climb the staircase. The order of the steps matters.

For example, if N is 4, then there are 5 unique ways:

1, 1, 1, 1
2, 1, 1
1, 2, 1
1, 1, 2
2, 2
What if, instead of being able to climb 1 or 2 steps at a time,
you could climb any number from a set of positive integers X? For example, if X = {1, 3, 5}, you could climb 1, 3, or 5 steps at a time.
"""
# We can solve this problem using dynamic programming.
# The idea is to maintain an array `dp` where `dp[i]` represents the number of unique ways to reach the i-th step.
# The base case is `dp[0] = 1` (one way to stay at the ground level).
# For each step from 1 to N, we iterate through the set X and for each x in X,
# if `i - x` is non-negative, we add `dp[i - x]` to `dp[i]`.
# This way, we build up the solution for each step based on the previous steps.
# Time complexity of O(N * |X|)
# Space complexity of O(N)
# where N is the number of steps and |X| is the size of the set X.
from typing import List


def count_ways(N: int, X: List[int]) -> int:
    dp = [0] * (N + 1)
    dp[0] = 1  # Base case: one way to stay at the ground level

    for i in range(1, N + 1):
        for x in X:
            if i - x >= 0:
                dp[i] += dp[i - x]

    return dp[N]

# Tests:
def test_count_ways():
    assert count_ways(4, [1, 2]) == 5
    assert count_ways(4, [1, 3, 5]) == 3
    assert count_ways(5, [1, 2]) == 8
    assert count_ways(5, [1, 3, 5]) == 5
    assert count_ways(0, [1, 2]) == 1
    assert count_ways(1, [1, 2]) == 1
    assert count_ways(2, [1, 2]) == 2
    assert count_ways(3, [1, 2]) == 3
    assert count_ways(10, [1, 2]) == 89
    assert count_ways(10, [1, 3, 5]) == 47
    print("All tests passed.")

# Example usage:
if __name__ == "__main__":
    test_count_ways()  # Run tests
    N = 4
    X = [1, 2]
    print(count_ways(N, X))  # Output: 5
