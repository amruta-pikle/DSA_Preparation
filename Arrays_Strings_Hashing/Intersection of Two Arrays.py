"""
Intersection of Two Arrays

Given two integer arrays nums1 and nums2, return an array of their intersection.
Each element in the result must be unique and you may return the result in any order.
"""

from typing import List


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """
        Returns the intersection of two arrays with unique elements.
        """
        common_nums = []

        for num in nums1:
            if num in nums2:
                common_nums.append(num)

        return list(set(common_nums))


# Example usage
if __name__ == "__main__":
    solution = Solution()

    nums1 = [1, 2, 2, 1]
    nums2 = [2, 2]
    print(solution.intersection(nums1, nums2))  # [2]

    nums3 = [4, 9, 5]
    nums4 = [9, 4, 9, 8, 4]
    print(solution.intersection(nums3, nums4))  # [9, 4] or [4, 9]
