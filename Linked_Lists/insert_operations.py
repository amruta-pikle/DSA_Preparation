class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_head(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_tail(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data, end = "->")
            temp = temp.next
        print("None")

if __name__ == "__main__":
    li = LinkedList()
    l2 = LinkedList()
    l3 = LinkedList()
    l4 = LinkedList()

    for value in [1]:
        li.insert_at_head(value)

    print("Linked List(at head:")
    li.print_list()
    print()

    for value in [1]:
        l2.insert_at_tail(value)

    print("Linked List(at tail:")
    l2.print_list()
    print()

    for value in []:
        l3.insert_at_head(value)

    print("Linked List(at head(empty):")
    l3.print_list()
    print()

    for value in []:
        l4.insert_at_tail(value)

    print("Linked List(at tail(empty):")
    l4.print_list()

