"""
Palindromic Substrings

Given a string s, return the number of palindromic substrings in it.

A string is a palindrome when it reads the same backward as forward.
A substring is a contiguous sequence of characters within the string.

Example 1:
Input: s = "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".

Example 2:
Input: s = "aaa"
Output: 6
Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".

Constraints:
1 <= s.length <= 1000
s consists of lowercase English letters.
"""

class Solution:
    def countSubstrings(self, s: str) -> int:
        """
        Counts the number of palindromic substrings in the given string.

        Approach (Expand Around Center):
        - Each palindrome has a center (can be one character or between two characters).
        - For each center, expand outward as long as the substring remains a palindrome.
        - Count all valid palindromic substrings.

        Time Complexity: O(n^2), where n = length of the string
        Space Complexity: O(1)
        """

        def expandAroundCenter(left: int, right: int) -> int:
            co
