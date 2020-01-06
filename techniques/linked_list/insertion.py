from techniques.linked_list.list_node import ListNode


def insert(node, x):
    current = node

    while current is not None:
        if current.next is None:
            current.next = ListNode(x)
            break
        else:
            if current.value < x < current.next.value:
                new_node = ListNode(x)
                new_node.next = current.next
                current.next = new_node
                break
        current = current.next

    current = node
    
    while current is not None:
        print(current.value)
        current = current.next


if __name__ == "__main__":
    l = ListNode(3)
    l.next = ListNode(4)
    l.next.next = ListNode(6)
    insert(l, 5)
