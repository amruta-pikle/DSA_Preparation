"""
234. Palindrome Linked List

Given the head of a singly linked list, return True if it is a palindrome, or False otherwise.

A palindrome is a sequence that reads the same backward as forward.

Example 1:
Input: head = [1,2,2,1]
Output: True

Example 2:
Input: head = [1,2]
Output: False

Constraints:
- The number of nodes in the list is in the range [1, 10^5].
- 0 <= Node.val <= 9
"""

from typing import Optional


class ListNode:
    """
    Definition for singly-linked list.
    """

    def __init__(self, val: int = 0, next: Optional["ListNode"] = None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        """
        Determines if a linked list is a palindrome.

        Approaches:

        1️⃣ Approach 1 (Optimal) — O(n) time, O(1) space:
            - Use slow and fast pointers to find the middle of the list.
            - Reverse the second half of the list.
            - Compare the first and second halves node by node.
            - (Optionally) Restore the list to its original form.

        2️⃣ Approach 2 (Simple) — O(n) time, O(n) space:
            - Store all node values in a list.
            - Check if the list equals its reverse.

        Returns:
            True if the linked list is a palindrome, else False.
        """

        # --- Approach 1: Optimal (Two-pointer + Reverse second half) ---
        if not head or not head.next:
            return True

        # Step 1: Find the middle of the linked list using slow and fast pointers
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Step 2: Reverse the second half of the list
        prev = None
        curr = slow
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        # Step 3: Compare both halves
        first = head
        second = prev
        while second:  # only need to compare till the end of second half
            if first.val != second.val:
                return False
            first = first.next
            second = second.next

        # If all matched, it’s a palindrome
        return True


class SolutionUsingList:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        """
        Approach 2 (Simple version) — O(n) time, O(n) space:
        Uses a list to store values and checks if the list equals its reverse.
        """

        values = []
        curr = head

        while curr:
            values.append(curr.val)
            curr = curr.next

        return values == values[::-1]


# --- Example usage ---
if __name__ == "__main__":
    # Build linked list [1, 2, 2, 1]
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(2)
    node4 = ListNode(1)
    node1.next = node2
    node2.next = node3
    node3.next = node4

    print("Optimal Approach (O(1) space):")
    print(Solution().isPalindrome(node1))  # Expected Output: True

    print("\nSimple Approach (O(n) space):")
    print(SolutionUsingList().isPalindrome(node1))  # Expected Output: True
