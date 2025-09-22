"""
Problem #13 [Hard]

This problem was asked by Amazon.

Given an integer k and a string s, find the length of the longest substring that contains at most k distinct characters.

For example, given s = "abcba" and k = 2, the longest substring with k distinct characters is "bcb".
"""
# We can use the sliding window technique to solve this problem.
# We will maintain a window that contains at most k distinct characters.
# We will use a dictionary to keep track of the count of each character in the current window.
# We will expand the window by moving the right pointer and adding characters to the dictionary.
# If the number of distinct characters exceeds k, we will shrink the window by moving the left
# pointer and removing characters from the dictionary until we are back to k distinct characters.
# We will keep track of the maximum length of the window during this process.
# Time complexity of O(n)
# Space complexity of O(k)
# where n is the length of the input string and k is the number of distinct characters allowed
from collections import defaultdict


def longest_substring_k_distinct(s: str, k: int) -> int:
    left = 0
    right = 0
    char_count = defaultdict(int)
    max_length = 0

    while right < len(s):
        char_count[s[right]] += 1

        while len(char_count) > k:
            char_count[s[left]] -= 1
            if char_count[s[left]] == 0:
                del char_count[s[left]]
            left += 1

        max_length = max(max_length, right - left + 1)
        right += 1

    return max_length

# Tests:
def test_longest_substring_k_distinct():
    assert longest_substring_k_distinct("abcba", 2) == 3  # "bcb"
    assert longest_substring_k_distinct("aaabbb", 1) == 3  # "aaa" or "bbb"
    assert longest_substring_k_distinct("aabbcc", 2) == 4  # "aabb", "bbcc", or "aacc"
    assert longest_substring_k_distinct("aabbcc", 3) == 6  # "aabbcc"
    assert longest_substring_k_distinct("aaaa", 1) == 4  # "aaaa"
    assert longest_substring_k_distinct("", 2) == 0  # empty string
    assert longest_substring_k_distinct("abcde", 5) == 5  # "abcde"
    assert longest_substring_k_distinct("abcde", 6) == 5  # "abcde"
    assert longest_substring_k_distinct("abaccc", 2) == 4  # "accc"
    print("All tests passed.")

# Example usage:
if __name__ == "__main__":
    test_longest_substring_k_distinct()  # Run tests
    s = "abcba"
    k = 2
    print(longest_substring_k_distinct(s, k))  # Output: 3
    s = "aaabbb"
    k = 1
    print(longest_substring_k_distinct(s, k))  # Output: 3
