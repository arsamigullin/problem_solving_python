# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:

        def successor(node):
            node = node.right
            while node.left:
                node = node.left
            return node.val

        def predecessor(node):
            node = node.left
            while node.right:
                node = node.right
            return node.val

        def delete(node, val):
            if not node:
                return None
            if node.val > val:
                node.left = delete(node.left, val)
            elif node.val < val:
                node.right = delete(node.right, val)
            else:
                if not node.left and not node.right:
                    node = None
                elif node.right:
                    node.val = successor(node)
                    node.right = delete(node.right, node.val)
                elif node.left:
                    node.val = predecessor(node)
                    node.left = delete(node.left, node.val)
            return node

        return delete(root, key)

