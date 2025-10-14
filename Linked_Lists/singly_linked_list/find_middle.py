class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

def find_middle(head):
    slow = head
    fast = head

    # this works for odd and for even if you want second middle node
    # while fast and fast.next:
    #     slow = slow.next
    #     fast = fast.next.next
    #
    # return slow.value

    # this works for odd and even if you want first middle node
    while fast and fast.next.next:
        slow = slow.next
        fast = fast.next.next

    return slow.value

head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
# head.next.next.next.next = Node(5)

print(find_middle(head))

