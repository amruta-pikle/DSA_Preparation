"""
242. Valid Anagram

Given two strings s and t, return True if t is an anagram of s, and False otherwise.
"""

from collections import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        Returns True if t is an anagram of s, else False.
        """
        # Using Counter to count characters in both strings
        return Counter(s) == Counter(t)

    # Brute force approach
    # if len(s) != len(t):
    #     return False
    # elif set(s)!=set(t):
    #     return False
    # else:
    #     s_count={}
    #     t_count={}
    #     w_set=set(s)
    #     for i in s:
    #         if i in s_count:
    #             s_count[i] += 1
    #         else:
    #             s_count[i] = 1

    #     for i in t:
    #         if i in t_count:
    #             t_count[i] += 1
    #         else:
    #             t_count[i] = 1

    #     for j in w_set:
    #         if s_count[j]!=t_count[j]:
    #             return False

    #     return True


# Example usage
if __name__ == "__main__":
    solution = Solution()

    print(solution.isAnagram("anagram", "nagaram"))  # True
    print(solution.isAnagram("rat", "car"))  # False
