# Definition for a Node.

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':

        if not root:
            return root

        listNode = head = Node()

        def helper(node):
            nonlocal listNode
            if not node:
                return

            helper(node.left)
            node.left = listNode
            listNode.right = node
            listNode = node
            helper(node.right)

        helper(root)

        # close DLL
        # the first node of head is dummy node
        # after running helper, listNode always points to the rightmost bottom item
        # head's right item points to the very first item of the sorted DLL
        listNode.right = head.right
        head.right.left = listNode

        return head.right

class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        def convertToDll(node):
            nonlocal first, last
            if node:
                convertToDll(node.left)
                if last:
                    last.right = node
                    node.left = last
                else:
                    first = node
                last = node
                convertToDll(node.right)
        if root is None:
            return root
        # first always points to the leftmost bottom item
        # last always points to the rightmost bottom item
        first, last = None, None
        convertToDll(root)

        # Close DLL
        last.right = first
        first.left = last
        return first