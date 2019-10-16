class ListNode:
    def __init__(self, value):
        self.val = value
        self.next = None


def isPalindrome(head):
    """
    :type head: ListNode
    :rtype: bool
    """
    curr = head
    count = 0
    while curr != None:
        curr = curr.next
        count += 1

    is_odd = count%2 == 1
    count = (count // 2 + 1) if count % 2 == 1 else count / 2

    curr = head
    prev = None
    next_ = None
    while count != 0:
        next_ = curr.next
        if count != 1 or is_odd == False:
            curr.next = prev
            prev = curr
        curr = next_
        count -= 1

    while next_ != None:
        if next_.val != prev.val:
            return False

        next_ = next_.next
        prev = prev.next

    return True

if __name__ == "__main__":
    l = ListNode(1)
    l.next = ListNode(0)
    #l.next = ListNode(0)
    l.next.next = ListNode(0)
    isPalindrome(l)


