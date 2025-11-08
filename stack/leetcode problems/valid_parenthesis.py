class Solution:
    """
    Solution class for validating parentheses using a stack.

    The input string contains only the characters '(', ')', '{', '}', '[' and ']'.
    A string is considered valid if:
        - Open brackets are closed by the same type of brackets.
        - Open brackets are closed in the correct order.
        - Every close bracket has a corresponding open bracket.
    """

    def isValid(self, s: str) -> bool:
        """
        Determines if the given string of parentheses is valid.

        Args:
            s (str): Input string consisting of parentheses.

        Returns:
            bool: True if the string is valid, False otherwise.
        """
        stack = []
        par_dict = {')': '(', '}': '{', ']': '['}

        for char in s:
            # If the character is a closing bracket
            if char in par_dict:
                top_element = stack.pop() if stack else '#'
                if par_dict[char] != top_element:
                    return False
            else:
                # It's an opening bracket
                stack.append(char)

        # If stack is empty, all brackets were matched correctly
        return not stack


if __name__ == "__main__":
    # Example test cases
    sol = Solution()
    test_cases = [
        ("()", True),
        ("()[]{}", True),
        ("(]", False),
        ("([])", True),
        ("([)]", False),
        ("[{]}", False),
        ("{[()]}", True),
    ]

    for s, expected in test_cases:
        print(f"Input: {s:10} → Output: {sol.isValid(s)} (Expected: {expected})")
