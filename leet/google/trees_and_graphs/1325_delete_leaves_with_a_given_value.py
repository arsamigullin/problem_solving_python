class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def removeLeafNodes(self, root: TreeNode, target: int) -> TreeNode:

        def helper(node):
            if not node:
                return True
            if helper(node.left): node.left = None
            if helper(node.right): node.right = None
            return node.val == target and node.left is None and node.right is None

        return None if helper(root) else root
