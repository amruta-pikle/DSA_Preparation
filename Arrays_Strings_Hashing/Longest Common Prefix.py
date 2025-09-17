"""
Longest Common Prefix

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:
Input: strs = ["flower","flow","flight"]
Output: "fl"

Example 2:
Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.

Constraints:
1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lowercase English letters if it is non-empty.
"""

from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        """
        Finds the longest common prefix among a list of strings.

        Approach:
        - Use the first string as a reference prefix.
        - For each character position, compare with all other strings.
        - Stop when a mismatch is found or a word ends.
        - Return the accumulated prefix.

        Time Complexity: O(N * M), where
            N = number of strings
            M = length of the shortest string
        Space Complexity: O(1)
        """
        if not strs:
            return ""

        prefix = strs[0]

        for i in range(len(prefix)):
            char = prefix[i]
            for word in strs[1:]:
                if i == len(word) or word[i] != char:
                    return prefix[:i]

        return prefix


# Example usage
if __name__ == "__main__":
    solution = Solution()

    print(solution.longestCommonPrefix(["flower", "flow", "flight"]))
    # "fl"

    print(solution.longestCommonPrefix(["dog", "racecar", "car"]))
    # ""
