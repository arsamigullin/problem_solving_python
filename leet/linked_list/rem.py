# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        prev = None
        cnt = 1
        node = head
        while node:
            if cnt %2 == 0:
                tmp = node.next
                prev.next = tmp
                node.next = prev
                node = tmp
            else:

                node = node.next
            prev = node
            cnt+=1
        return head

if __name__ == '__main__':
    root = ListNode(1)
    root.next = ListNode(2)
    root.next.next = ListNode(3)
    root.next.next.next = ListNode(4)
    root.next.next.next.next = ListNode(5)
    root.next.next.next.next.next = ListNode(6)
    s = Solution()
    s.swapPairs(root)