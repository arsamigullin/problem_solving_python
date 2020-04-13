# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# 538. Convert BST to Greater Tree
# https://leetcode.com/problems/convert-bst-to-greater-tree/
class Solution(object):
    '''
    Note: we have BST. So, all greatest node values lie on the right nodes
    that is why we start collect total from right node
    '''
    def convertBST(self, root):
        total = 0

        def dfs(node):
            nonlocal total
            if node:
                dfs(node.right)
                total += node.val
                node.val = total
                dfs(node.left)

        dfs(root)
        return root

# iteration solution
class Solution(object):
    def convertBST(self, root):
        total = 0

        node = root
        stack = []
        while stack or node is not None:
            # push all nodes up to (and including) this subtree's maximum on
            # the stack.
            while node is not None:
                stack.append(node)
                node = node.right

            node = stack.pop()
            total += node.val
            node.val = total

            # all nodes with values between the current and its parent lie in
            # the left subtree.
            node = node.left

        return root