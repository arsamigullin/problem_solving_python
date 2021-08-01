# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:

        cur, prev = head, None
        for _ in range(left - 1):
            prev = cur
            cur = cur.next

        front, tail = prev, cur

        # actual reversing
        while left <= right:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
            right -= 1

        # assign front properly
        if front:
            front.next = prev
        else:
            head = prev
        tail.next = cur
        return head
