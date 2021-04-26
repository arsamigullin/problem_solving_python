# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        successor = None

        while root:

            if p.val >= root.val:
                root = root.right
            else:
                successor = root
                root = root.left

        return successor


class Solution:
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':

        succ = None

        def helper(node):
            nonlocal succ
            if not node:
                return
            if p.val < node.val:
                succ = node
                helper(node.left)
            elif p.val >= node.val:
                helper(node.right)

        helper(root)
        return succ