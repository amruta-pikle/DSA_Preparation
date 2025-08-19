"""
Group Anagrams

Given an array of strings strs, group the anagrams together.
You can return the answer in any order.

"""
from collections import defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        word = defaultdict(list)

        for i in strs:
            key = ("".join(sorted(i)))
            word[key].append(i)

        return list(word.values())


if __name__ == "__main__":
    solution = Solution()
    str1 = ["eat","tea","tan","ate","nat","bat"]
    str2 = [""]
    str3 = ["a"]
    print(f"Group Anagrams for ['eat','tea','tan','ate','nat','bat'] are : {solution.groupAnagrams(str1)}")
    print(f"Group Anagrams for [''] are : {solution.groupAnagrams(str2)}")
    print(f"Group Anagrams for ['a'] are : {solution.groupAnagrams(str3)}")


