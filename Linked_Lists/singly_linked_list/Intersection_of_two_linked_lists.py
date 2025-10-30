class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        def get_length(head):
            length = 0
            while head:
                length += 1
                head = head.next
            return length

        lenA = get_length(headA)
        lenB = get_length(headB)

        diff = abs(lenA - lenB)

        if lenA > lenB:
            for _ in range(diff):
                headA = headA.next
        else:
            for _ in range(diff):
                headB = headB.next

        while headA and headB:
            if headA == headB:
                return headA
            headA = headA.next
            headB = headB.next

        return None


# Example setup:
# A: 4 -> 1 \
#              -> 8 -> 4 -> 5
# B:     5 -> 0 -> 1 /

common = ListNode(8, ListNode(4, ListNode(5)))

headA = ListNode(4, ListNode(1, common))
headB = ListNode(5, ListNode(0, ListNode(1, common)))

sol = Solution()
intersect = sol.getIntersectionNode(headA, headB)
print(intersect.val if intersect else None)  # Output: 8
