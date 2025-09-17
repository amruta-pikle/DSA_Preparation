"""
Subarray Sum Equals K

Given an array of integers nums and an integer k, return the total number of subarrays
whose sum equals to k.

A subarray is a contiguous non-empty sequence of elements within an array.

Example 1:
Input: nums = [1,1,1], k = 2
Output: 2

Example 2:
Input: nums = [1,2,3], k = 3
Output: 2
"""

from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        """
        Returns the total number of contiguous subarrays whose sum equals k.

        Approach:
        - Use prefix sums to keep track of the cumulative sum at each index.
        - Store prefix sums in a hashmap with their frequency.
        - If (prefix_sum - k) exists in the hashmap, it means there is a subarray
          that sums to k ending at the current index.
        """
        seen = {0: 1}  # Base case: prefix sum 0 has occurred once
        count = 0
        prefix_sum = 0

        for num in nums:
            prefix_sum += num

            if prefix_sum - k in seen:
                count += seen[prefix_sum - k]

            seen[prefix_sum] = seen.get(prefix_sum, 0) + 1

        return count


# Example usage
if __name__ == "__main__":
    solution = Solution()

    print(solution.subarraySum([1, 1, 1], 2))  # 2
    print(solution.subarraySum([1, 2, 3], 3))  # 2
    print(solution.subarraySum([3, 4, 7, 2, -3, 1, 4, 2], 7))  # 4
