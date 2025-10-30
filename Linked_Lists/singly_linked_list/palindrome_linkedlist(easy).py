class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        val = []
        curr = head

        while curr:
            val.append(curr.val)
            curr = curr.next

        return val == val[::-1]

def build_linked_list(values):
    head = ListNode(values[0])
    curr = head
    for val in values[1:]:
        curr.next = ListNode(val)
        curr = curr.next
    return head

head = build_linked_list([1,2,3,4])
sol = Solution()
print(sol.isPalindrome(head))

head2=build_linked_list([1,2,1])
print(sol.isPalindrome(head2))