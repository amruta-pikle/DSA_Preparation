"""
Valid Anagram

Given two strings s and t, return true if t is an anagram of s, and false otherwise.

Example 1:
Input: s = "anagram", t = "nagaram"
Output: true

Example 2:
Input: s = "rat", t = "car"
Output: false

Constraints:
1 <= s.length, t.length <= 5 * 10^4
s and t consist of lowercase English letters.
"""

from collections import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        Checks whether two strings are anagrams.

        Approach 1 (Manual Counting):
        - Count frequency of each character in both strings.
        - Compare the two frequency dictionaries.

        Approach 2 (Using collections.Counter):
        - Directly compare Counter(s) and Counter(t).

        Time Complexity: O(n), where n = length of the strings
        Space Complexity: O(1), since character set is fixed (26 lowercase letters)
        """
        return Counter(s) == Counter(t)


# Example usage
if __name__ == "__main__":
    solution = Solution()

    print(solution.isAnagram("anagram", "nagaram"))
    # True

    print(solution.isAnagram("rat", "car"))
    # False
