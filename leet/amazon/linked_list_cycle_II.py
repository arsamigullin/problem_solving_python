# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if head is None:
            return head

        def intersect(node):
            print('here')
            turtle = rabbit = node
            while rabbit and turtle:
                if rabbit.next is None:
                    return None
                rabbit = rabbit.next.next
                turtle = turtle.next
                if rabbit == turtle:
                    return turtle

            return None

        inters = intersect(head)
        if inters is None:
            return None

        ptr1 = inters
        ptr2 = head
        while ptr1 != ptr2:
            ptr1 = ptr1.next
            ptr2 = ptr2.next
        return ptr1
