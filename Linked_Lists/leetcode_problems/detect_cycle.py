"""
141. Linked List Cycle

Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again
by continuously following the next pointer. Internally, 'pos' is used to denote the index
of the node that tail's next pointer is connected to. Note that 'pos' is not passed as a parameter.

Return True if there is a cycle in the linked list. Otherwise, return False.

Example 1:
Input: head = [3,2,0,-4], pos = 1
Output: True
Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).

Example 2:
Input: head = [1,2], pos = 0
Output: True
Explanation: There is a cycle in the linked list, where the tail connects to the 0th node.

Example 3:
Input: head = [1], pos = -1
Output: False
Explanation: There is no cycle in the linked list.

Constraints:
- The number of nodes in the list is in the range [0, 10^4].
- -10^5 <= Node.val <= 10^5
- pos is -1 or a valid index in the linked-list.
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
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        """
        Detects whether a linked list has a cycle using Floyd’s Cycle Detection Algorithm.

        Uses two pointers (slow and fast):
        - slow moves one step at a time
        - fast moves two steps at a time

        If there’s a cycle, they will eventually meet at some node.
        If fast or fast.next becomes None, there’s no cycle.
        """
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            # If both pointers meet, a cycle exists
            if slow == fast:
                return True

        # No cycle found
        return False


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
    node4.next = node2  # cycle here

    # Check for cycle
    solution = Solution()
    print(solution.hasCycle(node1))  # Expected Output: True
