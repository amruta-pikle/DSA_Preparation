"""
Maximum Subarray

Given an integer array nums, find the subarray with the largest sum,
and return its sum.

This is solved using Kadane’s Algorithm, which runs in O(n) time.
"""

from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """
        Returns the maximum subarray sum using Kadane's Algorithm.

        At each step, it decides whether to extend the current subarray
        or start a new one from the current element.
        """
        curr_sum = nums[0]
        max_sum = nums[0]

        for i in range(1, len(nums)):
            # Either start new subarray at nums[i], or extend current subarray
            curr_sum = max(nums[i], curr_sum + nums[i])
            max_sum = max(max_sum, curr_sum)

        return max_sum


# Example usage
if __name__ == "__main__":
    solution = Solution()

    print(solution.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))  # 6
    print(solution.maxSubArray([1]))                             # 1
    print(solution.maxSubArray([5, 4, -1, 7, 8]))                # 23
