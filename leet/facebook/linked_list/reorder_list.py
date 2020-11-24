# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution1:
    # Algo is the following
    # 1. put each node to the dictionary where keys are incremental number
    # 2. define middle of the next traversal
    # 3.  L0→Ln→L1→Ln-1→L2→Ln-2→…
    # travers while i>0. Inside loop we store node.next in tmp then replace the node.next with d[n] then we update
    # d[n].next and node with tmp
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        d = {}
        n = 0
        node = head
        # 1
        while node is not None:
            d[n] = node
            n += 1
            node = node.next
        node = head
        # 2
        i = n // 2 + n % 2
        # 3
        while i > 0:
            n -= 1
            tmp = node.next
            node.next = d[n]
            if i > 1:
                d[n].next = tmp
            else:
                d[n].next = None # do not forget to reset next of the latest node
            node = tmp
            i -= 1


class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head:
            return None

        d = {}
        n = 0

        node = head
        while node:
            d[n] = node
            n += 1
            node = node.next

        root = node = d[0]
        b = 0
        i = 0
        j = n - 1
        while b < n:

            if b % 2 == 0:
                node.next = d[j]
                i += 1
            else:
                node.next = d[i]
                j -= 1
            node = node.next
            b += 1

        node.next = None
        return root


if __name__ == "__main__":
    l1 = ListNode(1)
    l1.next = ListNode(2)
    l1.next.next = ListNode(3)
    l1.next.next.next = ListNode(4)
    s = Solution()
    s.reorderList(l1)
