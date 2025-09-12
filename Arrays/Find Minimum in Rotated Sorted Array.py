"""
Find Minimum in Rotated Sorted Array

Suppose an array of length n sorted in ascending order is rotated between 1 and n times.
Given the sorted rotated array nums of unique elements, return the minimum element of this array.

You must write an algorithm that runs in O(log n) time.
"""

from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        """
        Returns the minimum element in a rotated sorted array.

        Uses binary search (O(log n)) to find the pivot point where
        the rotation occurs, which corresponds to the minimum element.
        """
        low, high = 0, len(nums) - 1

        # If array has only one element
        if low == high:
            return nums[0]

        while low < high:
            mid = (low + high) // 2

            # If mid element > rightmost element,
            # minimum must be in the right half
            if nums[mid] > nums[high]:
                low = mid + 1
            else:
                # Otherwise, minimum is in the left half (including mid)
                high = mid

        return nums[low]


# Example usage
if __name__ == "__main__":
    solution = Solution()

    print(solution.findMin([3, 4, 5, 1, 2]))       # 1
    print(solution.findMin([4, 5, 6, 7, 0, 1, 2])) # 0
    print(solution.findMin([11, 13, 15, 17]))      # 11
