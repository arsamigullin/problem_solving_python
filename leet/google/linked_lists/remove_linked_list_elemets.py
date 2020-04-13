# thil problem
# https://leetcode.com/problems/remove-linked-list-elements/
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class SolutionBad:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        if not head:
            return head
        res = []
        node = head
        while node:
            if node.val != val:
                res.append(node)
            node = node.next
        for i in range(len(res) - 1):
            res[i].next = res[i + 1]
        if res:
            res[-1].next = None
            return res[0]
        return None

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        sentinel = ListNode(-1)
        sentinel.next = head
        prev, cur = sentinel, head
        while cur:
            # once it equals the val
            if cur.val == val:
                # the next of prev is the next of cur
                # thereby we avoid the cur
                # NOTE: prev itself is not changed
                # so if the val of next cur is again val, we override prev.next
                prev.next = cur.next
            else:
                prev = cur
            cur = cur.next
        return  sentinel.next

if __name__ == "__main__":
    # 1->2->6->3->4->5->6
    l = ListNode(1)
    l.next = ListNode(2)
    l.next.next = ListNode(6)
    l.next.next.next = ListNode(3)
    l.next.next.next.next = ListNode(4)
    l.next.next.next.next.next = ListNode(5)
    l.next.next.next.next.next.next = ListNode(6)
    s = Solution()
    s.removeElements(l, 6)

