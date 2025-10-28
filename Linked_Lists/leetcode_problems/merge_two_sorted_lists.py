"""
21. Merge Two Sorted Lists

You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list.
The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

Example 1:
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

Example 2:
Input: list1 = [], list2 = []
Output: []

Example 3:
Input: list1 = [], list2 = [0]
Output: [0]

Constraints:
- The number of nodes in both lists is in the range [0, 50].
- -100 <= Node.val <= 100
- Both list1 and list2 are sorted in non-decreasing order.
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
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        """
        Merges two sorted linked lists into a single sorted linked list.

        Uses a dummy head node to simplify pointer handling.
        Returns the merged list starting from dummy.next.
        """
        dummy = ListNode()  # Dummy placeholder node (val=0 by default)
        curr = dummy

        # Traverse both lists and merge nodes in sorted order
        while list1 and list2:
            if list1.val < list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next

            curr = curr.next

        # Append the remaining nodes of whichever list is not empty
        curr.next = list1 if list1 else list2

        return dummy.next


# Example usage
if __name__ == "__main__":
    # Build first linked list [1, 2, 4]
    list1 = ListNode(1)
    list1.next = ListNode(2)
    list1.next.next = ListNode(4)

    # Build second linked list [1, 3, 4]
    list2 = ListNode(1)
    list2.next = ListNode(3)
    list2.next.next = ListNode(4)

    # Merge the lists
    solution = Solution()
    merged_head = solution.mergeTwoLists(list1, list2)

    # Print merged linked list
    curr = merged_head
    while curr:
        print(curr.val, end=" -> ")
        curr = curr.next
    print("None")  # Expected Output: 1 -> 1 -> 2 -> 3 -> 4 -> 4 -> None
