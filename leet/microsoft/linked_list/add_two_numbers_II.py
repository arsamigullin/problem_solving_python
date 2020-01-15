# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# This is recursive solution.
# Before we want to know the length each of list
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:

        def get_lenght(node):
            n = node
            length = 0
            while n:
                n = n.next
                length += 1
            return length

        len_1 = get_lenght(l1)
        len_2 = get_lenght(l2)

        def add(node1, node2, n1, n2):
            if node1 is None and node2 is None:
                return (None, 0)
            if n1 == n2:
                nextNode, rem = add(node1.next, node2.next, n1 - 1, n2 - 1)
                total = node1.val + node2.val + rem
            elif n1 > n2:
                nextNode, rem = add(node1.next, node2, n1 - 1, n2)
                total = node1.val + rem
            else:
                nextNode, rem = add(node1, node2.next, n1, n2 - 1)
                total = node2.val + rem
            d, r = divmod(total, 10)
            curr = ListNode(r)
            curr.next = nextNode
            return (curr, d)

        node, rem = add(l1, l2, len_1, len_2)
        if rem > 0:
            ans = ListNode(rem)
            ans.next = node
            return ans
        return node