# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        node = head
        while node is not None and node.next is not None:
            if node.val == node.next.val:
                node.next = node.next.next
            else:
                node = node.next

        return head


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        node = head
        resnode = res = ListNode(float('inf'))

        while node:
            if resnode.val != node.val:
                resnode.next = node
                resnode = resnode.next
            node = node.next
            resnode.next = None
        return res.next