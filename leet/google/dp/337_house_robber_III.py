# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
# this tightly coupled with Solution2 of 198_House_Robber.py
class Solution:
    def rob(self, root: TreeNode) -> int:
        if not root:
            return 0

        def dfs(node):
            if not node:
                return 0, 0

            lmax, lpmax = dfs(node.left)
            rmax, rpmax = dfs(node.right)

            curmax = lmax + rmax
            prevmax = lpmax + rpmax

            return max(curmax, prevmax + node.val), curmax

        return dfs(root)[0]

