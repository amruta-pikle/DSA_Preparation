"""
160. Intersection of Two Linked Lists

Given the heads of two singly linked lists headA and headB,
return the node at which the two lists intersect.
If the two linked lists have no intersection at all, return None.

Note:
The linked lists must retain their original structure after the function returns.

Example 1:
Input: intersectVal = 8,
       listA = [4,1,8,4,5],
       listB = [5,6,1,8,4,5],
       skipA = 2, skipB = 3
Output: Intersected at '8'

Example 2:
Input: intersectVal = 2,
       listA = [1,9,1,2,4],
       listB = [3,2,4],
       skipA = 3, skipB = 1
Output: Intersected at '2'

Example 3:
Input: intersectVal = 0,
       listA = [2,6,4],
       listB = [1,5],
       skipA = 3, skipB = 2
Output: No intersection

Constraints:
- The number of nodes of listA is in the range [1, 3 * 10^4].
- The number of nodes of listB is in the range [1, 3 * 10^4].
- 1 <= Node.val <= 10^5
- 0 <= skipA <= m
- 0 <= skipB <= n
- intersectVal is 0 if the lists do not intersect,
  otherwise intersectVal == listA[skipA] == listB[skipB].

Follow up:
Can you write a solution that runs in O(m + n) time and uses O(1) memory?
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
    def getIntersectionNode(
        self, headA: Optional[ListNode], headB: Optional[ListNode]
    ) -> Optional[ListNode]:
        """
        Returns the node at which two singly linked lists intersect.
        Uses a two-pointer technique with O(1) extra memory and O(m + n) time.
        If there is no intersection, returns None.
        """
        if not headA or not headB:
            return None

        a, b = headA, headB

        # Traverse both lists; when one reaches the end, redirect to the other list’s head
        while a != b:
            a = a.next if a else headB
            b = b.next if b else headA

        # When they meet, it's the intersection node or None if no intersection
        return a


# Example usage
if __name__ == "__main__":
    # Build two linked lists that intersect
    # A: 4 -> 1 \
    #              -> 8 -> 4 -> 5
    # B:    5 -> 6 -> 1 /
    intersect = ListNode(8, ListNode(4, ListNode(5)))

    headA = ListNode(4, ListNode(1, intersect))
    headB = ListNode(5, ListNode(6, ListNode(1, intersect)))

    solution = Solution()
    intersection_node = solution.getIntersectionNode(headA, headB)

    if intersection_node:
        print(f"Intersected at '{intersection_node.val}'")
    else:
        print("No intersection")
