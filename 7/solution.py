"""
Problem #7 [Medium]

This problem was asked by Facebook.

Given the mapping a = 1, b = 2, ... z = 26,
and an encoded message, count the number of ways it can be decoded.

For example, the message '111' would give 3,
since it could be decoded as 'aaa', 'ka', and 'ak'.

You can assume that the messages are decodable.
For example, '001' is not allowed.
"""
# We can solve this problem using dynamic programming.
# We will maintain an array dp where dp[i] represents the number of ways to decode the
# substring of length i. The base case is dp[0] = 1 (an empty string has one way to be decoded).
# For each character in the string, we will check if it can form a valid single-digit
# or two-digit number with the previous character. If it can, we will add the number of ways
# to decode the substring up to the previous character(s) to dp[i].
# Time complexity of O(n)
# Space complexity of O(n)
# where n is the length of the input string.
from typing import List


def num_decodings(s: str) -> int:
    if not s or s[0] == '0':
        return 0

    n = len(s)
    dp: List[int] = [0] * (n + 1)
    dp[0] = 1  # Base case: empty string
    dp[1] = 1  # Base case: first character (not '0')

    for i in range(2, n + 1):
        one_digit = int(s[i - 1:i])  # Last one digit
        two_digit = int(s[i - 2:i])  # Last two digits

        if 1 <= one_digit <= 9:
            dp[i] += dp[i - 1]
        if 10 <= two_digit <= 26:
            dp[i] += dp[i - 2]

    return dp[n]

# A more space-efficient solution would involve using two variables to keep track of
# the last two values of dp instead of maintaining the entire dp array.
# This would reduce the space complexity to O(1).
def num_decodings_optimized(s: str) -> int:
    if not s or s[0] == '0':
        return 0

    n = len(s)
    prev2 = 1  # dp[0]
    prev1 = 1  # dp[1]

    for i in range(2, n + 1):
        current = 0
        one_digit = int(s[i - 1:i])  # Last one digit
        two_digit = int(s[i - 2:i])  # Last two digits

        if 1 <= one_digit <= 9:
            current += prev1
        if 10 <= two_digit <= 26:
            current += prev2

        prev2, prev1 = prev1, current

    return prev1

# Tests:
def test_num_decodings():
    assert num_decodings('111') == 3
    assert num_decodings('12') == 2
    assert num_decodings('226') == 3
    assert num_decodings('0') == 0
    assert num_decodings('06') == 0
    assert num_decodings('10') == 1
    assert num_decodings('27') == 1
    assert num_decodings('11106') == 2
    assert num_decodings('123456789') == 3

    assert num_decodings_optimized('111') == 3
    assert num_decodings_optimized('12') == 2
    assert num_decodings_optimized('226') == 3
    assert num_decodings_optimized('0') == 0
    assert num_decodings_optimized('06') == 0
    assert num_decodings_optimized('10') == 1
    assert num_decodings_optimized('27') == 1
    assert num_decodings_optimized('11106') == 2
    assert num_decodings_optimized('123456789') == 3

# Example usage:
if __name__ == "__main__":
    test_num_decodings() # Run tests
    s = '111'
    print(num_decodings(s))  # Output: 3
    print(num_decodings_optimized(s))  # Output: 3
