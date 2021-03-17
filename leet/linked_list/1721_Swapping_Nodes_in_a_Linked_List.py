# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapNodes(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return head
        arr = []
        node = head
        second = first = None

        while node:
            # arr.append(node)
            if second:
                second = second.next
            if k == 1:
                first = node
                second = head
            k -= 1
            node = node.next
        first.val, second.val = second.val, first.val
        return head