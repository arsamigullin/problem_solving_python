# Definition for a binary tree node.
import bisect
# This problem
# https://leetcode.com/problems/binary-tree-longest-consecutive-sequence-ii/
# 549. Binary Tree Longest Consecutive Sequence II

# Similar problem
# https://leetcode.com/problems/binary-tree-longest-consecutive-sequence/
#298. Binary Tree Longest Consecutive Sequence
import math


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


class Solution:
    def longestConsecutive(self, root: TreeNode) -> int:
        res = 0

        def dfs(node, par):
            nonlocal res
            if not node:
                return 0, 0
            inc = int(node.val + 1 == par)
            dec = int(node.val - 1 == par)
            linc, ldec = dfs(node.left, node.val)
            rinc, rdec = dfs(node.right, node.val)
            res = max(linc + rdec + 1, ldec + rinc + 1, res)
            return 0 if inc == 0 else max(linc, rinc) + 1, 0 if dec == 0 else max(ldec, rdec) + 1

        l, r = dfs(root, float('-inf'))
        return max(res, l, r)


class Solution:
    def longestConsecutive(self, root) -> int:

        res = 0

        def helper(node, par_val):
            nonlocal res
            if not node:
                return 0, 0
            lef_dec, left_inc = helper(node.left, node.val)
            right_dec, right_inc = helper(node.right, node.val)
            res = max(res, lef_dec + right_inc + 1, right_dec + left_inc + 1)
            incr = 0
            if node.val - par_val == 1:
                incr = max(left_inc, right_inc) + 1
            dec = 0
            if node.val - par_val == -1:
                dec = max(lef_dec, right_dec) + 1
            return dec, incr

        dec, incr = helper(root, root.val)
        return max(res, dec, incr)


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestConsecutive(self, root) -> int:
        res = 0
        def helper(node, par):
            nonlocal res
            if not node:
                return 0,0 #
            increment = int(par + 1 == node.val)
            decrement = int(par - 1 == node.val)
            left_decrement, left_increment = helper(node.left, node.val)
            rigt_decrement, right_increment = helper(node.right, node.val)
            # U-shape check
            res=max(res, left_decrement + right_increment + 1, left_increment + rigt_decrement + 1)
            # check the branches
            dec = 0 if decrement==0 else max(left_decrement, rigt_decrement) + 1
            inc = 0 if increment==0 else max(left_increment, right_increment) + 1
            return dec,inc
        dec, inc = helper(root, math.inf)
        return max(res, dec, inc)