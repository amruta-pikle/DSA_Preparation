"""
Group Anagrams

Given an array of strings strs, group the anagrams together.
You can return the answer in any order.

Example 1:
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Example 2:
Input: strs = [""]
Output: [[""]]

Example 3:
Input: strs = ["a"]
Output: [["a"]]

Constraints:
1 <= strs.length <= 10^4
0 <= strs[i].length <= 100
strs[i] consists of lowercase English letters.
"""

from collections import defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        Groups words that are anagrams of each other.

        Approach:
        - Use a hashmap (defaultdict) where the key is the sorted version of the string.
          Example: "eat" -> "aet"
        - Append each word to the list corresponding to its sorted key.
        - Return all grouped lists.

        Time Complexity: O(n * k log k), where
            n = number of strings
            k = maximum length of a string (due to sorting)
        Space Complexity: O(n * k), to store grouped anagrams.
        """
        word_map = defaultdict(list)

        for word in strs:
            key = "".join(sorted(word))  # Sorting ensures anagrams share the same key
            word_map[key].append(word)

        return list(word_map.values())


# Example usage
if __name__ == "__main__":
    solution = Solution()

    print(solution.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
    # [["eat","tea","ate"],["tan","nat"],["bat"]]

    print(solution.groupAnagrams([""]))
    # [[""]]

    print(solution.groupAnagrams(["a"]))
    # [["a"]]
