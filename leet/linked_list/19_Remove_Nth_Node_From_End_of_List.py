# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode()
        dummy.next = head
        left = dummy
        right = head
        cnt = 0

        while right:
            cnt += 1
            if cnt > n:
                left = left.next
            right = right.next

        left.next = None if not left.next else left.next.next
        return dummy.next
