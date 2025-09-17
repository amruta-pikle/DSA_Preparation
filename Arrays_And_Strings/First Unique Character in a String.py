"""
First Unique Character in a String

Given a string s, find the first non-repeating character in it and return its index.
If it does not exist, return -1.

Example 1:
Input: s = "leetcode"
Output: 0
Explanation: The character 'l' at index 0 is the first character that does not occur at any other index.

Example 2:
Input: s = "loveleetcode"
Output: 2

Example 3:
Input: s = "aabb"
Output: -1
"""

class Solution:
    def firstUniqChar(self, s: str) -> int:
        """
        Returns the index of the first non-repeating character in the string.
        If none exists, returns -1.

        Approach:
        - Count the frequency of each character in the string.
        - Iterate again through the string and return the index of the first
          character with frequency 1.
        """
        char_freq = {}

        # Count frequencies
        for ch in s:
            char_freq[ch] = char_freq.get(ch, 0) + 1

        # Find first unique
        for i, ch in enumerate(s):
            if char_freq[ch] == 1:
                return i

        return -1


# Example usage
if __name__ == "__main__":
    solution = Solution()

    print(solution.firstUniqChar("leetcode"))      # 0
    print(solution.firstUniqChar("loveleetcode"))  # 2
    print(solution.firstUniqChar("aabb"))          # -1
