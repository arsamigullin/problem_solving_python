# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maximumAverageSubtree(self, root: TreeNode) -> float:
        max_val = 0

        def helper(node):
            nonlocal max_val
            if not node:
                return 0, 0
            l, cl = helper(node.left)
            r, cr = helper(node.right)
            tot = l + r + node.val
            cnt = cl + cr + 1
            max_val = max(max_val, tot / cnt)
            return tot, cnt

        helper(root)
        return max_val