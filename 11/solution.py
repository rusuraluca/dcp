"""
Problem #11 [Medium]

This problem was asked by Twitter.

Implement an autocomplete system. That is, given a query string s and a set of all possible query strings, return all strings in the set that have s as a prefix.

For example, given the query string de and the set of strings [dog, deer, deal], return [deer, deal].

Hint: Try preprocessing the dictionary into a more efficient data structure to speed up queries.
"""
# We can implement the autocomplete system using a Trie (prefix tree) data structure.
# The Trie will allow us to efficiently store and retrieve strings based on their prefixes.
# We will define a TrieNode class to represent each node in the Trie and a Trie class
# to handle the insertion and searching of words.
# The autocomplete function will traverse the Trie based on the given prefix
# and collect all words that match the prefix.
# Time complexity of O(m + n)
# Space complexity of O(k)
# where m is the length of the prefix, n is the number of words with the given prefix,
# and k is the total number of characters in the Trie.
from typing import List, Dict


class TrieNode:
    def __init__(self):
        self.children: Dict[str, 'TrieNode'] = {}
        self.is_end_of_word: bool = False

class Trie:
    def __init__(self):
        self.root: TrieNode = TrieNode()

    def insert(self, word: str) -> None:
        current: TrieNode = self.root
        for char in word:
            if char not in current.children:
                current.children[char] = TrieNode()
            current = current.children[char]
        current.is_end_of_word = True

    def autocomplete(self, prefix: str) -> List[str]:
        current: TrieNode = self.root
        for char in prefix:
            if char not in current.children:
                return []
            current = current.children[char]

        # Collect all words that match the prefix
        results: List[str] = []
        self._collect_words(current, prefix, results)
        return results

    def _collect_words(self, node: TrieNode, prefix: str, results: List[str]) -> None:
        if node.is_end_of_word:
            results.append(prefix)
        for char, child in node.children.items():
            self._collect_words(child, prefix + char, results)

def autocomplete_system(s: str, words: List[str]) -> List[str]:
    trie = Trie()
    for word in words:
        trie.insert(word)
    return trie.autocomplete(s)

# Tests:
def test_autocomplete_system():
    words = ['dog', 'deer', 'deal']
    assert sorted(autocomplete_system('de', words)) == ['deal', 'deer']
    assert sorted(autocomplete_system('do', words)) == ['dog']
    assert sorted(autocomplete_system('a', words)) == []
    assert sorted(autocomplete_system('', words)) == ['deal', 'deer', 'dog']
    print("All tests passed!")

# Example usage:
if __name__ == "__main__":
    test_autocomplete_system() # Run tests
    words = ['dog', 'deer', 'deal']
    print(autocomplete_system('de', words))  # Output: ['deer', 'deal']
    print(autocomplete_system('do', words))  # Output: ['dog']
    print(autocomplete_system('a', words))   # Output: []
    print(autocomplete_system('', words))    # Output: ['dog', 'deer', 'deal']
