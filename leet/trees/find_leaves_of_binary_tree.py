# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findLeaves(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        res = []
        removed_nodes = []

        def remove_leaves(node):
            if node is None:
                return False
            if node.left is None and node.right is None:
                removed_nodes.append(node.val)
                return True

            if remove_leaves(node.left):
                node.left = None

            if remove_leaves(node.right):
                node.right = None

            return False

        while root.left is not None or root.right is not None:
            remove_leaves(root)
            res.append(removed_nodes)
            removed_nodes = []
        res.append([root.val])
        return res

# quite interesting solution
# we define dictionary where keys are levels
# level starts enumerating from the bottom
# for example
#     1 ()
#    / \
#   2   3 lvl of 3 is 1, lvl of 2 is 2
#  / \
# 4   5 level = max(lvl of 4, lvl of 5) = 1

import collections
class Solution(object):
    def findLeaves(self, root):
        def order(root, dic):
            if not root:
                return 0
            left = order(root.left, dic)
            right = order(root.right, dic)
            lev = max(left, right) + 1
            dic[lev] += root.val,
            return lev
        dic, ret = collections.defaultdict(list), []
        order(root, dic)
        for i in range(1, len(dic) + 1):
            ret.append(dic[i])
        return ret