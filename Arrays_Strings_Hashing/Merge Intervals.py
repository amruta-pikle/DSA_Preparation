"""
Merge Intervals

Given an array of intervals where intervals[i] = [starti, endi],
merge all overlapping intervals, and return an array of the
non-overlapping intervals that cover all the intervals in the input.
"""

from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """
        Merges all overlapping intervals and returns a list of
        non-overlapping intervals that cover the input.
        """
        # Sort intervals based on the start value
        intervals.sort(key=lambda x: x[0])

        merged = []
        for interval in intervals:
            # If merged is empty or there is no overlap, add the interval
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                # Overlapping intervals → merge them
                merged[-1][1] = max(merged[-1][1], interval[1])

        return merged


# Example usage
if __name__ == "__main__":
    solution = Solution()

    intervals1 = [[1, 3], [2, 6], [8, 10], [15, 18]]
    print(solution.merge(intervals1))  # [[1, 6], [8, 10], [15, 18]]

    intervals2 = [[1, 4], [4, 5]]
    print(solution.merge(intervals2))  # [[1, 5]]

    intervals3 = [[4, 7], [1, 4]]
    print(solution.merge(intervals3))  # [[1, 7]]
