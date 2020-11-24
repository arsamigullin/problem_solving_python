# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        # this fast slow pointer technique to find middle of the list
        def getMid(head):
            prevslow = None
            slow = fast = head
            while fast and fast.next:
                prevslow = slow
                slow = slow.next
                fast = fast.next.next
            prevslow.next = None
            return slow

        def sort(head):
            if not head or not head.next:
                return head
            mid = getMid(head)
            l = sort(head)
            r = sort(mid)
            return merge(l, r)

        def merge(first, second):
            dummyHead = ListNode()
            tail = dummyHead
            while first and second:
                if first.val > second.val:
                    tail.next = second
                    second = second.next
                    tail = tail.next
                else:
                    tail.next = first
                    first = first.next
                    tail = tail.next
            if first:
                tail.next = first
            if second:
                tail.next = second
            return dummyHead.next

        return sort(head)