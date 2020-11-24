class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next


class SolutionMy:
    def insert(self, head: 'Node', insertVal: int) -> 'Node':
        if not head:
            tmp = Node(insertVal)
            tmp.next = tmp
            return tmp
        min_Node = None
        max_Node = None
        cnt = 0
        node = head
        while cnt < 2:
            if node == head:
                cnt += 1
            if not min_Node or node.val < min_Node.val:
                min_Node = node
            if not max_Node or node.val >= max_Node.val:
                max_Node = node
            node = node.next

        if min_Node.val <= insertVal <= max_Node.val:
            prev = head
            cur = prev.next
            while True:
                if prev.val <= insertVal <= cur.val:
                    tmp = prev.next
                    prev.next = Node(insertVal, tmp)
                    return head
                prev = cur
                cur = cur.next
        elif insertVal < min_Node.val:
            tmp = max_Node.next
            max_Node.next = Node(insertVal, tmp)

        return head


class Solution:
    def insert(self, head: 'Node', insertVal: int) -> 'Node':
        if not head:
            tmp = Node(insertVal)
            tmp.next = tmp
            return tmp
        prev = head
        cur = head.next
        while True:
            if prev.val <= insertVal <= cur.val:
                tmp = prev.next
                prev.next = Node(insertVal, tmp)
                return head
            if prev.val > cur.val and (insertVal < cur.val or insertVal > prev.val):
                tmp = prev.next
                prev.next = Node(insertVal, tmp)
                return head
            prev = cur
            cur = cur.next

            if prev == head:
                break

        prev.next = Node(insertVal, cur)
        return head
