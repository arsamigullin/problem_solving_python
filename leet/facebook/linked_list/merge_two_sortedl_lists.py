# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None and l2 is None:
            return None

        head = l3 = ListNode(0)

        while l1 and l2:

            if l1.val >= l2.val:
                l3.next = l2 # note, we referring to the node entirely
                l2 = l2.next
            else:
                l3.next = l1 # note, we referring to the node entirely
                l1 = l1.next

            l3 = l3.next # do not forget to increase l3

        if l1:
            l3.next = l1
        if l2:
            l3.next = l2
        return head.next
