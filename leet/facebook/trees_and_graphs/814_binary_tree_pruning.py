# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pruneTree(self, root: TreeNode) -> TreeNode:
        def helper(node):
            if not node:
                return False
            node.left = None if not helper(node.left) else node.left
            node.right = None if not helper(node.right) else node.right
            return node.val == 1 or not node.left is None or not node.right is None

        return root if helper(root) else None
