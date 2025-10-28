class  Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def build_linked_list(values):
    if not values:
        return None

    head = Node(values[0])
    current = head
    for val in values[1:]:
        current.next = Node(val)
        current = current.next
    return head

def print_linked_list(head):
    current = head
    while current:
        print(current.val, end=" -> " if current.next else "")
        current = current.next
    print()

class Solution:
    def mergeTwoLists(self, list1, list2):
        dummy = Node()
        current = dummy

        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next

            current = current.next

        current.next = list1 if list1 else list2
        return dummy.next

# Build input linked lists
list1 = build_linked_list([1, 2, 4])
list2 = build_linked_list([1, 3, 4])

# printing lists
print_linked_list(list1)
print_linked_list(list2)

# Merge them
solution = Solution()
merged_head = solution.mergeTwoLists(list1, list2)

# Print the merged result
print("Merged Linked List:")
print_linked_list(merged_head)
