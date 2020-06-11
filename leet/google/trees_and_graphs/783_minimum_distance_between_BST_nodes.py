# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def minDiffInBST(self, root: TreeNode) -> int:

        arr = []

        def helper(node):
            if not node:
                return
            helper(node.left)
            arr.append(node.val)
            helper(node.right)

        helper(root)
        min_val = float('inf')
        for i in range(1, len(arr)):
            min_val = min(min_val, arr[i] - arr[i - 1])
        return min_val


class Solution(object):
    def minDiffInBST(self, root):
        def dfs(node):
            if node:
                dfs(node.left)
                self.ans = min(self.ans, node.val - self.prev)
                self.prev = node.val
                dfs(node.right)

        self.prev = float('-inf')
        self.ans = float('inf')
        dfs(root)
        return self.ans