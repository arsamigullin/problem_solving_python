# Definition for singly-linked list.
import collections


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicatesUnsorted(self, head: ListNode) -> ListNode:

        if not head:
            return head

        node = head
        dups = collections.defaultdict(int)

        while node:
            dups[node.val] += 1
            node = node.next

        node = result = ListNode()

        while head:
            if dups[head.val] == 1:
                node.next = ListNode(head.val)
                node = node.next
            head = head.next

        return result.next