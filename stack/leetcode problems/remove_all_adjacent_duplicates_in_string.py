class Solution:
    """
    Solution class for removing all adjacent duplicates in a string using a stack.

    The input string consists of lowercase English letters.
    A duplicate removal consists of removing two adjacent and equal letters.
    This process is repeated until no more adjacent duplicates exist.
    """

    def removeDuplicates(self, s: str) -> str:
        """
        Removes all adjacent duplicates from the input string.

        Args:
            s (str): Input string consisting of lowercase English letters.

        Returns:
            str: The final string after all duplicate removals.
        """
        stack = []

        for ch in s:
            # If the stack is empty or the top element is not equal to current char
            if not stack or ch != stack[-1]:
                stack.append(ch)
            else:
                # Current char is equal to the top element → remove duplicate
                stack.pop()

        # Convert stack back to string
        return "".join(stack)


if __name__ == "__main__":
    # Example test cases
    sol = Solution()
    test_cases = [
        ("abbaca", "ca"),
        ("azxxzy", "ay"),
        ("a", "a"),
        ("", ""),
        ("aabbcc", ""),  # all removed
        ("abccba", ""),  # cascading removals
    ]

    for s, expected in test_cases:
        result = sol.removeDuplicates(s)
        print(f"Input: {s:10} → Output: {result} (Expected: {expected})")
