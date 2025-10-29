"""
142. Linked List Cycle II

Given the head of a linked list, return the node where the cycle begins.
If there is no cycle, return None.

There is a cycle in a linked list if there is some node in the list that can be
reached again by continuously following the next pointer. Internally, 'pos' is used
to denote the index of the node that tail's next pointer is connected to (0-indexed).
It is -1 if there is no cycle. Note that 'pos' is not passed as a parameter.

Do not modify the linked list.

Example 1:
Input: head = [3,2,0,-4], pos = 1
Output: tail connects to node index 1
Explanation: There is a cycle in the linked list, where tail connects to the second node.

Example 2:
Input: head = [1,2], pos = 0
Output: tail connects to node index 0
Explanation: There is a cycle in the linked list, where tail connects to the first node.

Example 3:
Input: head = [1], pos = -1
Output: no cycle
Explanation: There is no cycle in the linked list.

Constraints:
- The number of nodes in the list is in the range [0, 10^4].
- -10^5 <= Node.val <= 10^5
- pos is -1 or a valid index in the linked list.
"""

from typing import Optional


class ListNode:
    """
    Definition for singly-linked list.
    """

    def __init__(self, x: int):
        self.val = x
        self.next: Optional["ListNode"] = None


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Detects the node where the cycle begins using Floyd’s Cycle Detection Algorithm (Tortoise and Hare).

        Step 1: Use two pointers (slow and fast).
                - slow moves one step at a time.
                - fast moves two steps at a time.
                If they meet, a cycle exists.

        Step 2: To find the cycle’s starting node:
                - Move one pointer to the head.
                - Keep the other at the meeting point.
                - Move both one step at a time.
                The node where they meet again is the start of the cycle.

        Returns:
            The node where the cycle begins, or None if no cycle exists.
        """
        slow = head
        fast = head

        # Step 1: Detect if a cycle exists
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                break
        else:
            # No cycle found
            return None

        # Step 2: Find the start of the cycle
        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next

        return slow


# Example usage
if __name__ == "__main__":
    # Create nodes
    node1 = ListNode(3)
    node2 = ListNode(2)
    node3 = ListNode(0)
    node4 = ListNode(-4)

    # Connect nodes to form a cycle: 3 -> 2 -> 0 -> -4 -> 2
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node2  # cycle
