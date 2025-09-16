"""
Two Sum

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer i
"""
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        com_dict = {}

        for i, num in enumerate(nums):
            compliment = target - num
            if compliment in com_dict:
                return [com_dict[compliment], i]
            else:
                com_dict[num] = i

if __name__ == "__main__":
    solution = Solution()
    i1,i2 = solution.twoSum([2,7,11,15],9)
    print(f"Indices for [2,7,11,15] are : {i1,i2}")