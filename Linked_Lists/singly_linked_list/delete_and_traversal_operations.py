class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    # Insert at tail of the building list
    def insert_at_tail(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return

        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = new_node

    # Print List
    def print_list(self):
        curr = self.head
        if not curr:
            print("List is empty")

        while curr:
            print(curr.data, end=" -> ")
            curr = curr.next
        print("None")

    # Length of list
    def length(self):
        count = 0
        curr = self.head
        while curr:
            count += 1
            curr = curr.next
        return count

    # search for the value
    def search(self, key):
        curr = self.head
        position = 0

        while curr:
            if curr.data == key:
                return position
            curr = curr.next
            position += 1

        return -1  # Not found

    # Delete a node by value
    def delete_node(self, key):
        curr = self.head
        prev = None

        # if head needs to be deleted
        if curr and curr.data == key:
            self.head = curr.next
            curr = None
            return

        # Search for the node to delete
        while curr and curr.data != key:
            prev = curr
            curr = curr.next

        if not curr:
            print(f"{key} not found in the list")
            return

        # Delete the node
        prev.next = curr.next
        curr = None


if __name__ == "__main__":
    # Create Linked List
    ll = LinkedList()
    for i in [10, 20, 30, 40, 50]:
        ll.insert_at_tail(i)

    print("Original List:")
    ll.print_list()

    # Length
    print("Length:", ll.length())

    # Search
    print("Position of 30:", ll.search(30))
    print("Position of 100:", ll.search(100))

    # Delete head
    print("\nDelete head (10):")
    ll.delete_node(10)
    ll.print_list()

    # Delete middle node
    print("\nDelete middle node (30):")
    ll.delete_node(30)
    ll.print_list()

    # Delete tail
    print("\nDelete tail (50):")
    ll.delete_node(50)
    ll.print_list()

    # Try deleting a non-existing node
    print("\nDelete non-existing node (100):")
    ll.delete_node(100)
    ll.print_list()
