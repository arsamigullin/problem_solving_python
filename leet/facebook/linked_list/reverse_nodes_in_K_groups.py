# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# since we shouldn't touch the inconsistent group (the group where k is not equals count of nodes,
# usually this is latest group)
# first we want to know how many groups we have

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:

        node = head
        node_count = 0
        while node:
            node = node.next
            node_count += 1
        group_cnt = node_count // k
        def find(node, group_num):
            if group_num > group_cnt:
                return node
            if node is None:
                return None
            i=0
            current = first = node
            # this is usual reverse we use to reverse linked list
            # we do reverse until we less than k
            # or node is None
            prev = None
            while i < k and current is not None:
                temp = current.next
                current.next = prev
                prev = current
                current = temp
                i+=1
            # at this time the current will be pointing to the following nodes
            # prev will be containing the k nodes in reverse order
            # and we need to tie the first element (we stored at the beginning)
            # with the rest nodes
            first.next = find(current, group_num + 1)
            return prev

        res = find(head, 1)
        return res
if __name__ == "__main__":
    s = Solution()
    l = ListNode(1)
    l.next = ListNode(2)
    l.next.next = ListNode(3)
    l.next.next.next = ListNode(4)
    l.next.next.next.next = ListNode(5)
    s.reverseKGroup(l, 3)