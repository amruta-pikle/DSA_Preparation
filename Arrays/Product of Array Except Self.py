"""
Product of Array Except Self

Given an integer array nums, return an array answer such that answer[i] is equal
to the product of all the elements of nums except nums[i].

You must write an algorithm that runs in O(n) time and without using the division operation.
"""

from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        Returns an array where each element is the product of all other elements in nums.

        Approach:
        - First pass (prefix): Store the product of all elements to the left of each index.
        - Second pass (suffix): Multiply by the product of all elements to the right.

        This ensures O(n) time complexity and O(1) extra space (ignoring the output array).
        """
        n = len(nums)
        answer = [1] * n

        # Compute prefix products
        prefix = 1
        for i in range(n):
            answer[i] = prefix
            prefix *= nums[i]

        # Compute suffix products and multiply into answer
        suffix = 1
        for i in range(n - 1, -1, -1):
            answer[i] *= suffix
            suffix *= nums[i]

        return answer


# Example usage
if __name__ == "__main__":
    solution = Solution()

    print(solution.productExceptSelf([1, 2, 3, 4]))  # [24, 12, 8, 6]
    print(solution.productExceptSelf([-1, 1, 0, -3, 3]))  # [0, 0, 9, 0, 0]
