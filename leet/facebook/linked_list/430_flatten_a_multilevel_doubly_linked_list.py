# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child


class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        '''
        we want to keep track of first and last nodes of the current chunk of the linked list
        '''
        if not head:
            return None
        node = head
        def helper(node):
            first  = node
            last = None
            while node:
                if node.child:
                    # having first and last nodes of the chunk started from node.child
                    # we want to merge it to the current linked list
                    #
                    f, l = helper(node.child)
                    # to cover the cases where node.next is None
                    # we mark as last node the l from child's linked list
                    # 1-2-3
                    #     \
                    #      4-5
                    # since 3.next is None, the last node will be node 5
                    last = l
                    tmp = node.next
                    node.next = f
                    f.prev = node
                    l.next = tmp
                    if tmp:
                        tmp.prev = l
                    # do not forget to null child node
                    node.child = None
                    node = tmp
                else:
                    last = node
                    node = node.next
            return first, last
        helper(node)
        return head


"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""


class Solution(object):
    def flatten(self, head):
        if not head:
            return

        pseudoHead = Node(0, None, head, None)
        prev = pseudoHead

        stack = []
        stack.append(head)

        while stack:
            curr = stack.pop()

            prev.next = curr
            curr.prev = prev

            if curr.next:
                stack.append(curr.next)

            if curr.child:
                stack.append(curr.child)
                # don't forget to remove all child pointers.
                curr.child = None

            prev = curr
        # detach the pseudo head node from the result.
        pseudoHead.next.prev = None
        return pseudoHead.next