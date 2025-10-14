class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def find_node(head):
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if fast == slow:
            break
    else:
        return None

    slow = head
    while slow != fast:
        slow = slow.next
        fast = fast.next

    return slow

head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
#head.next.next.next = head

cycle_start = find_node(head)
if cycle_start:
    print(cycle_start.data)
else:
    print("No cycle")
