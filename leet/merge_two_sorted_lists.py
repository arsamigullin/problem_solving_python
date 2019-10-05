    
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def mergeTwoLists(l1: ListNode, l2: ListNode) -> ListNode:
    merged = None
    first = l1
    second = l2
    if l1.val > l2.val:
        merged = l2
        first = l1
        second = l2.next
    else:
        merged = l1
        second = l2
        first = l1.next
    mi = merged
    while second is not None or first is not None:
        if second is None:
            mi.next = first
            first = first.next
        elif first is None:
            mi.next = second
            second = second.next
        else:
            if first.val > second.val:
                mi.next = second
                second = second.next
            else:
                mi.next = first
                first = first.next
        mi = mi.next
    return merged


l1 = ListNode(1)
l1.next = ListNode(2)
l1.next.next = ListNode(4)
   

l2 = ListNode(2)
l2.next = ListNode(3)
l2.next.next = ListNode(4)
l2.next.next.next = ListNode(5)
if __name__ == "__main__":
    mergeTwoLists(l1,l2)