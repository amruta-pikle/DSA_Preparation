"""
206. Reverse Linked List

Given the head of a singly linked list, reverse the list, and return the reversed list.

Example 1:
Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]

Example 2:
Input: head = [1,2]
Output: [2,1]

Example 3:
Input: head = []
Output: []

Constraints:
- The number of nodes in the list is in the range [0, 5000].
- -5000 <= Node.val <= 5000
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
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Reverses a singly linked list and returns the new head.
        Uses iterative pointer manipulation.
        """
        prev = None
        curr = head

        while curr:
            next_node = curr.next  # store reference to next node
            curr.next = prev       # reverse the pointer
            prev = curr            # move prev one step forward
            curr = next_node       # move curr one step forward

        return prev


# Example usage
if __name__ == "__main__":
    # Build linked list [1, 2, 3, 4, 5]
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)

    # Reverse linked list
    solution = Solution()
    reversed_head = solution.reverseList(head)

    # Print reversed list
    curr = reversed_head
    while curr:
        print(curr.val, end=" -> ")
        curr = curr.next
    print("None")   # Output: 5 -> 4 -> 3 -> 2 -> 1 -> None
