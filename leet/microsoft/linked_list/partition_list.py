# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
# https://leetcode.com/problems/partition-list/
# 1. We keep two lists one store the left side nodes the second one store the right side lists
# 2. Depending on current value we fill left and right list
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
        r.next = None # do not forget to reset the latest node pointer
        l.next = right.next
        return left.next