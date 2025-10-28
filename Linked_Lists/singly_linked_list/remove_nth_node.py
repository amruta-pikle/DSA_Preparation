class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Remove_nth_node:

    def __init__(self):
        self.head = None
    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        curr = self.head

        while curr.next:
            curr = curr.next
        curr.next = new_node

    def print_list(self,):
        curr = self.head
        while curr:
            print(curr.val, end=" -> ")
            curr = curr.next
        print("None")

    def remove_nth_node(self, head: Node, n: int):
        dummy = Node(0)
        dummy.next = head

        fast = dummy
        slow = dummy

        for _ in range(n):
            fast = fast.next

        while fast.next:
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next

        return dummy.next

if __name__ == "__main__":
    l1 = Remove_nth_node()

    l1.insert_at_end(1)
    l1.insert_at_end(2)
    l1.insert_at_end(3)
    l1.insert_at_end(4)
    l1.insert_at_end(5)
    l1.insert_at_end(6)

    print("Before removing 2nd node from end")
    l1.print_list()
    print()

    l1.head = l1.remove_nth_node(l1.head, 2)
    print("After removing 2nd node from end")
    l1.print_list()
    print()


