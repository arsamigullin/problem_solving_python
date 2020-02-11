# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class MySolution:
    def middleNode(self, head: ListNode) -> ListNode:
        count = 0
        node = head
        while node:
            node = node.next
            count+=1
        middle = count//2
        node = head
        while middle > 0:
            node = node.next
            middle-=1
        return node

# Fast and slow pointers solution
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def middleNode(self, head):
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow