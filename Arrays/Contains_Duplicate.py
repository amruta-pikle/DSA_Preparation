"""
Contains Duplicate

Given an integer array nums, return True if any value appears at least twice in the array,
and False if every element is distinct.
"""

from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        """
        Returns True if nums contains duplicates, else False.
        """
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False


# Example usage
if __name__ == "__main__":
    solution = Solution()

    print(solution.containsDuplicate([1, 2, 3, 1]))  # True
    print(solution.containsDuplicate([1, 2, 3, 4]))  # False
    print(solution.containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))  # True
