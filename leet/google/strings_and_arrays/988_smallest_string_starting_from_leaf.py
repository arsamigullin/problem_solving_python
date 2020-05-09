# Definition for a binary tree node.
import string


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def smallestFromLeaf(self, root: TreeNode) -> str:
        smallest = string.ascii_lowercase[::-1]

        def helper(node, val):
            nonlocal smallest
            val = chr(97 + node.val) + val
            if node.left is None and node.right is None:
                smallest = min(smallest, val)
            if node.left:
                helper(node.left, val)
            if node.right:
                helper(node.right, val)

        helper(root, '')
        return smallest


class Solution:
    def smallestFromLeaf(self, root: TreeNode) -> str:
        smallest = string.ascii_lowercase[::-1]

        stack = [(root, '')]
        while stack:
            node, val = stack.pop()
            if node:
                val = chr(97 + node.val) + val
                if not node.left and not node.right:
                    smallest = min(smallest, val)
                else:
                    stack.append((node.left, val))
                    stack.append((node.right, val))
        return smallest

