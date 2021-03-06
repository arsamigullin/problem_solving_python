# Definition for a binary tree node.

# This problem
# https://leetcode.com/problems/binary-tree-longest-consecutive-sequence-ii/
# 549. Binary Tree Longest Consecutive Sequence II

# Similar problem
# https://leetcode.com/problems/binary-tree-longest-consecutive-sequence/
#298. Binary Tree Longest Consecutive Sequence
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def longestConsecutive(self, root: TreeNode) -> int:
        if not root:
            return 0
        _max = 0
        def dfs(node):
            nonlocal _max
            if not node:
                return 0,0
            inc, dec = 1, 1
            if node.left:
                incL, decL = dfs(node.left)
                if node.val == node.left.val + 1:
                    dec = decL + 1
                elif node.val == node.left.val - 1:
                    inc = incL + 1
            if node.right:
                incR, decR = dfs(node.right)
                if node.val == node.right.val + 1:
                    dec = max(dec, decR + 1)
                elif node.val == node.right.val -1:
                    inc = max(inc, incR + 1) 
            _max = max(_max, dec + inc - 1)
            return inc, dec
        dfs(root)
        return _max


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    """
    DFS: using two variables increase, decrease to represent how many consecutive increasing / decreasing values this node has
    """

    def longestConsecutive(self, root: TreeNode) -> int:
        self.res = 0
        self.dfs(root)
        return self.res

    def dfs(self, root):
        if not root:
            # incresing, decreasing
            return (0, 0)

        icr, dcr = 1, 1

        if root.left:
            i, d = self.dfs(root.left)
            if root.val == root.left.val + 1:
                dcr = d + 1
            elif root.val == root.left.val - 1:
                icr = i + 1

        if root.right:
            i, d = self.dfs(root.right)
            if root.val == root.right.val + 1:
                dcr = max(dcr, d + 1)
            elif root.val == root.right.val - 1:
                icr = max(icr, i + 1)

        self.res = max(self.res, icr + dcr - 1)

        return (icr, dcr)