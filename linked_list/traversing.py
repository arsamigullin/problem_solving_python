from linked_list.list_node import ListNode

def traverse(node):
    current = node
    while current != None:
        print(current.value)
        current = current.next

if __name__ == "__main__":
    l = ListNode(3)
    l.next = ListNode(4)
    l.next.next = ListNode(5)
    traverse(l)
