class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_tail(self,data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return

        curr = self.head

        while curr.next:
            curr = curr.next
        curr.next = new_node

    def print_list(self):
        if not self.head:
            print("List is empty!")

        curr = self.head
        while curr:
            print(curr.data, end=" ->")
            curr = curr.next
        print("None")

    def reverse_list(self):
        prev = None
        curr = self.head

        while curr:
            next_node = curr.next
            curr.next = prev
            prev=curr
            curr=next_node

        self.head = prev

if __name__ == "__main__":
    ll = LinkedList()
    for i in [1, 2, 3, 4, 5]:
        ll.insert_at_tail(i)

    print("Original List:")
    ll.print_list()

    ll.reverse_list()
    print("Reversed Iteratively:")
    ll.print_list()



