# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# This is recursive solution.
# Before we want to know the length each of list
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:

        def reversell(head):
            node = head
            prev = None
            while node:
                nxt = node.next
                node.next = prev
                prev = node
                node = nxt
            return prev

        l1 = reversell(l1)
        l2 = reversell(l2)

        carry = 0
        result = None
        while l1 or l2 or carry > 0:
            if l1:
                carry += l1.val
                l1 = l1.next

            if l2:
                carry += l2.val
                l2 = l2.next

            l3 = ListNode(carry % 10)
            l3.next = result
            result = l3
            carry = carry // 10

        if carry > 0:
            l3 = ListNode(carry % 10)
            l3.next = result
            result = l3

        return result