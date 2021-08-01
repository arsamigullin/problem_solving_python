# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class SolutionShort:
    def swapNodes(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return head
        arr = []
        node = head
        second = first = None

        while node:
            # arr.append(node)
            if second:
                second = second.next
            if k == 1:
                first = node
                second = head
            k -= 1
            node = node.next
        first.val, second.val = second.val, first.val
        return head

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapNodes(self, head: ListNode, k: int) -> ListNode:
        dummy = ListNode()
        dummy.next = head
        node=dummy
        nodeList = []
        while node:
            nodeList.append(node)
            node = node.next
        n = len(nodeList)
        first = nodeList[k]
        second = nodeList[n-k]
        if first.next == second:
            second_next = second.next
            second.next = first
            first.next = second_next
            nodeList[k - 1].next = second
        elif second.next == first:
            first_next = first.next
            second.next = first_next
            first.next = second
            nodeList[n-k-1].next = first
        else:
            first_next = first.next
            second_next = second.next
            nodeList[n-k-1].next = first
            first.next = second_next
            second.next = first_next
            nodeList[k-1].next = second
        return dummy.next

if __name__ == '__main__':
    s = Solution()
    root = ListNode(1)
    root.next = ListNode(2)
    s.swapNodes(root, 2)