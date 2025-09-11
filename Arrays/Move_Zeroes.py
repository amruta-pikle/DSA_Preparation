"""
Move Zeroes

Given an integer array nums, move all 0's to the end of it while maintaining
the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.
"""

from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Modifies nums in-place to move all zeroes to the end
        while keeping the relative order of non-zero elements.
        """
        k = 0  # pointer for the next non-zero position
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[k] = nums[k], nums[i]
                k += 1


# Example usage
if __name__ == "__main__":
    solution = Solution()

    nums1 = [0, 1, 0, 3, 12]
    solution.moveZeroes(nums1)
    print(nums1)  # [1, 3, 12, 0, 0]

    nums2 = [0]
    solution.moveZeroes(nums2)
    print(nums2)  # [0]

    nums3 = [4, 2, 4, 0, 0, 3, 0, 5, 1, 0]
    solution.moveZeroes(nums3)
    print(nums3)  # [4, 2, 4, 3, 5, 1, 0, 0, 0, 0]
