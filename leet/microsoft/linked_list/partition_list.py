# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        if head == None:
            return head
        l = left = ListNode(0)
        r = right = ListNode(0)

        node = head
        while node:
            if node.val < x:
                l.next = node
                l = l.next
            else:
                r.next = node
                r = r.next
            node = node.next
        r.next = None
        l.next = right.next
        return left.next