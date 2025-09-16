"""
Rotate Array

Given an integer array nums, rotate the array to the right by k steps,
where k is non-negative.
"""

from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Rotates the array to the right by k steps in-place.

        Args:
            nums (List[int]): The list of integers to rotate.
            k (int): Number of steps to rotate the array.

        Returns:
            None: The function modifies the input list in-place.
        """
        n = len(nums)
        k %= n  # handle cases where k >= n
        nums[:] = nums[-k:] + nums[:-k]


# Example usage
if __name__ == "__main__":
    solution = Solution()

    nums1 = [1, 2, 3, 4, 5, 6, 7]
    solution.rotate(nums1, 3)
    print(nums1)  # [5, 6, 7, 1, 2, 3, 4]

    nums2 = [-1, -100, 3, 99]
    solution.rotate(nums2, 2)
    print(nums2)  # [3, 99, -1, -100]
