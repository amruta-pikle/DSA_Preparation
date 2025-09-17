"""
Two Sum

Given an array of integers nums and an integer target, return indices of the two numbers
such that they add up to target.

You may assume that each input would have exactly one solution, and you may not
use the same element twice.

You can return the answer in any order.

Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:
Input: nums = [3,3], target = 6
Output: [0,1]
"""

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Returns the indices of the two numbers that add up to target.

        Approach:
        - Use a hashmap (dictionary) to store numbers and their indices.
        - For each number, compute its complement (target - num).
        - If the complement has already been seen, return the indices.
        - Otherwise, store the current number in the hashmap.
        """
        com_dict = {}

        for i, num in enumerate(nums):
            compliment = target - num
            if compliment in com_dict:
                return [com_dict[compliment], i]
            com_dict[num] = i


# Example usage
if __name__ == "__main__":
    solution = Solution()

    print(solution.twoSum([2, 7, 11, 15], 9))  # [0, 1]
    print(solution.twoSum([3, 2, 4], 6))       # [1, 2]
    print(solution.twoSum([3, 3], 6))          # [0, 1]
