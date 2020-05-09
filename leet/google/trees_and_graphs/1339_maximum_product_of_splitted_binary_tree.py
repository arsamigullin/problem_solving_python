# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
# in case of we have restriction with 32 bit number
# it is much better to use this approach
class Solution:
    def maxProduct(self, root: TreeNode) -> int:

        def findtotal(node):
            if not node:
                return 0
            return node.val + findtotal(node.left) + findtotal(node.right)
        total = findtotal(root)
        _max = 0
        _min = float('inf')
        def dfs(node):
            nonlocal _max, _min
            if not node:
                return 0
            cur = node.val + dfs(node.left) + dfs(node.right)
            diff = abs((total - cur) - cur)
            if _min > diff:
                _min = diff
                _max = ((total - cur) * cur)%(10**9+7)
            return cur
        dfs(root)
        return _max



class Solution:
    def maxProduct(self, root: TreeNode) -> int:

        def findtotal(node):
            if not node:
                return 0
            return node.val + findtotal(node.left) + findtotal(node.right)
        total = findtotal(root)
        _max = 0
        def dfs(node):
            nonlocal _max
            if not node:
                return 0
            cur = node.val + dfs(node.left) + dfs(node.right)
            _max = max(_max, (total - cur) * cur)
            return cur
        dfs(root)
        return _max%(10**9+7)