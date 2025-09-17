"""
Remove Duplicates from Sorted Array

Given an integer array nums sorted in non-decreasing order, remove the
duplicates in-place such that each unique element appears only once.
The relative order of the elements should be kept the same.

Then return the number of unique elements in nums.

The first k elements of nums should contain the unique elements, and
the rest can be ignored.
"""

from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """
        Removes duplicates from a sorted array in-place.

        Args:
            nums (List[int]): A sorted list of integers.

        Returns:
            int: The number of unique elements (k).
        """
        if not nums:
            return 0

        k = 1  # index for placing unique elements
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[k] = nums[i]
                k += 1

        return k


# Example usage
if __name__ == "__main__":
    solution = Solution()

    nums1 = [1, 1, 2]
    k1 = solution.removeDuplicates(nums1)
    print(k1, nums1[:k1])  # 2 [1, 2]

    nums2 = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    k2 = solution.removeDuplicates(nums2)
    print(k2, nums2[:k2])  # 5 [0, 1, 2, 3, 4]
