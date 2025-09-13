"""
Longest Substring Without Repeating Characters

Given a string s, find the length of the longest substring without repeating characters.

Example 1:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

Constraints:
0 <= s.length <= 5 * 10^4
s consists of English letters, digits, symbols and spaces.
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Returns the length of the longest substring without repeating characters.

        Approach (Sliding Window / Two Pointers):
        - Use two pointers (`left` and `right`) to define the current window.
        - Maintain a set of characters in the current window.
        - Expand `right` pointer to include new characters.
        - If a duplicate character is found, move the `left` pointer forward
          while removing characters from the set until the duplicate is gone.
        - Track the maximum window size observed.

        Time Complexity: O(n), where n is the length of the string.
        Space Complexity: O(k), where k is the character set size (bounded by ASCII).
        """
        char_set = set()
        left = 0
        max_length = 0

        for right in range(len(s)):
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1

            char_set.add(s[right])
            max_length = max(max_length, right - left + 1)

        return max_length


# Example usage
if __name__ == "__main__":
    solution = Solution()

    print(solution.lengthOfLongestSubstring("abcabcbb"))  # 3
    print(solution.lengthOfLongestSubstring("bbbbb"))     # 1
    print(solution.lengthOfLongestSubstring("pwwkew"))    # 3
