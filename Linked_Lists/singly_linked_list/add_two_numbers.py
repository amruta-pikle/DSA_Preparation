class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode()
        curr = dummy
        carry = 0

        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            total = val1 + val2 + carry

            carry = total // 10
            curr.next = ListNode(total % 10)

            curr = curr.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next

def create_linked_list(values):
    """Convert a list into a linked list."""
    dummy = ListNode()
    curr = dummy
    for val in values:
        curr.next = ListNode(val)
        curr = curr.next
    return dummy.next


def print_linked_list(head):
    """Print the linked list in readable format."""
    vals = []
    while head:
        vals.append(str(head.val))
        head = head.next
    print(" -> ".join(vals))


# ---------- Test Example ----------

# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
l1 = create_linked_list([2, 4, 3])
l2 = create_linked_list([5, 6, 4])

sol = Solution()
result = sol.addTwoNumbers(l1, l2)

print("Result:")
print_linked_list(result)