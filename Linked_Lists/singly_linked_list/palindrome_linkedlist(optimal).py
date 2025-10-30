class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head and not head.next:
            return True

        fast = slow = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        prev=None
        curr = slow

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        first = head
        second = prev

        while second:
            if first.val != second.val:
                return False
            first = first.next
            second = second.next

        return True

def build_linked_list(values):
    head = ListNode(values[0])
    curr = head
    for val in values[1:]:
        curr.next = ListNode(val)
        curr = curr.next
    return head

head = build_linked_list([1,2,1])
sol = Solution()
print(sol.isPalindrome(head))

head2 = build_linked_list([1,2,2,1])
print(sol.isPalindrome(head2))


