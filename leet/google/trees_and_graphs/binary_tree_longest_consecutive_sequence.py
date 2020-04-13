# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# This problem
# https://leetcode.com/problems/binary-tree-longest-consecutive-sequence/
#298. Binary Tree Longest Consecutive Sequence

# Similar problem
# https://leetcode.com/problems/binary-tree-longest-consecutive-sequence-ii/
# 549. Binary Tree Longest Consecutive Sequence II


class Solution:
    def longestConsecutive(self, root: TreeNode) -> int:
        _max = 0

        def dfs(node):
            nonlocal _max
            if not node:
                return 0
            inc = 1
            if node.left:
                incL = dfs(node.left)
                if node.val == node.left.val - 1:
                    inc = incL + 1
            if node.right:
                incR = dfs(node.right)
                if node.val == node.right.val - 1:
                    inc = max(inc, incR + 1)
            _max = max(_max, inc)
            return inc

        dfs(root)
        return _max