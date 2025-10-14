"""
876. Middle of the Linked List

Given the head of a singly linked list, return the middle node of the linked list.

If there are two middle nodes, return the second middle node.

Example 1:
Input: head = [1,2,3,4,5]
Output: [3,4,5]

Example 2:
Input: head = [1,2,3,4,5,6]
Output: [4,5,6]

Constraints:
- The number of nodes in the list is in the range [1, 100].
- 1 <= Node.val <= 100
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
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Returns the middle node of a singly linked list.
        If the list has two middle nodes, returns the second one.
        Uses the slow and fast pointer technique.
        """
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow


# Example usage
if __name__ == "__main__":
    # Build linked list [1, 2, 3, 4, 5, 6]
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    head.next.next.next.next.next = ListNode(6)

    # Find middle node
    solution = Solution()
    middle = solution.middleNode(head)

    # Print middle sublist
    curr = middle
    while curr:
        print(curr.val, end=" -> ")
        curr = curr.next
    print("None")  # Output: 4 -> 5 -> 6 -> None
