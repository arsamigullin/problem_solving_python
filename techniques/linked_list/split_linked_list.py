class ListNode:
    def __init__(self, value):
        self.val = value
        self.next = None

# this algo is incorrect
def split_linked_list(head):
    """
    :type head: ListNode
    :rtype: bool
    """

    slow = head
    fast = head.next
    while fast:
        fast = fast.next
        while fast:
            fast = fast.next
            slow = slow.next
    a = head
    b = slow.next
    slow.next = None
    return slow

    return True

if __name__ == "__main__":
    l = ListNode(1)
    l.next = ListNode(2)
    #l.next = ListNode(0)
    l.next.next = ListNode(3)
    l.next.next.next = ListNode(2)
    l.next.next.next.next = ListNode(1)
    split_linked_list(l)
