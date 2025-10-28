"""
19. Remove Nth Node From End of List

Given the head of a linked list, remove the nth node from the end of the list and return its head.

Example 1:
Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]

Example 2:
Input: head = [1], n = 1
Output: []

Example 3:
Input: head = [1,2], n = 1
Output: [1]

Constraints:
- The number of nodes in the list is sz.
- 1 <= sz <= 30
- 0 <= Node.val <= 100
- 1 <= n <= sz
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
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """
        Removes the nth node from the end of a singly linked list and returns the new head.
        Uses a two-pointer (fast and slow) approach with a dummy node to handle edge cases cleanly.
        """

        # Create a dummy node before the head to simplify edge cases (like removing the first node)
        dummy = ListNode(0)
        dummy.next = head

        fast = dummy
        slow = dummy

        # Move fast pointer n steps ahead
        for _ in range(n):
            fast = fast.next

        # Move both pointers until fast reaches the end
        while fast.next:
            fast = fast.next
            slow = slow.next

        # Remove the nth node
        slow.next = slow.next.next

        return dummy.next


# Example usage
if __name__ == "__main__":
    # Build linked list [1, 2, 3, 4, 5]
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)

    n = 2

    # Remove nth node from end
    solution = Solution()
    new_head = solution.removeNthFromEnd(head, n)

    # Print updated list
    curr = new_head
    while curr:
        print(curr.val, end=" -> ")
        curr = curr.next
    print("None")  # Expected output: 1 -> 2 -> 3 -> 5 -> None
