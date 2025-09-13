"""
Valid Palindrome

A phrase is a palindrome if, after converting all uppercase letters into lowercase
letters and removing all non-alphanumeric characters, it reads the same forward
and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

Example 1:
Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.

Example 2:
Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.

Example 3:
Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.

Constraints:
1 <= s.length <= 2 * 10^5
s consists only of printable ASCII characters.
"""

import re


class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        Returns True if the given string is a palindrome, False otherwise.

        Approach 1 (Regex + Two Pointers):
        - Convert the string to lowercase.
        - Remove all non-alphanumeric characters using regex.
        - Use two pointers (`left` and `right`) to check characters from both ends.
        - If all corresponding characters match, return True.

        Time Complexity: O(n), where n is the length of the string.
        Space Complexity: O(n), due to storing the cleaned string.
        """
        lowercase = s.lower()
        clean_s = re.sub(r'[^a-zA-Z0-9]', '', lowercase)
        left, right = 0, len(clean_s) - 1

        while left < right:
            if clean_s[left] != clean_s[right]:
                return False
            left += 1
            right -= 1

        return True


# Optimal Version (No extra space for cleaned string)
class OptimalSolution:
    def isPalindrome(self, s: str) -> bool:
        """
        Optimized approach without creating a cleaned string:
        - Use two pointers (`left` and `right`).
        - Skip non-alphanumeric characters.
        - Compare lowercase characters directly.
        - Stop early if mismatch found.

        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        left, right = 0, len(s) - 1

        while left < right:
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1

            if s[left].lower() != s[right].lower():
                return False

            left += 1
            right -= 1

        return True


# Example usage
if __name__ == "__main__":
    solution = Solution()
    optimal = OptimalSolution()

    print(solution.isPalindrome("A man, a plan, a canal: Panama"))  # True
    print(solution.isPalindrome("race a car"))                      # False
    print(solution.isPalindrome(" "))                               # True

    print(optimal.isPalindrome("A man, a plan, a canal: Panama"))   # True
    print(optimal.isPalindrome("race a car"))                       # False
    print(optimal.isPalindrome(" "))                                # True
