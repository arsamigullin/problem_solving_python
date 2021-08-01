# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import List


class Solution:
    def findLeaves(self, root: TreeNode) -> List[List[int]]:

        def dfs(node, lvs):
            if not node:
                return None
            if not node.left and not node.right:
                lvs.append(node.val)
                return None
            node.left = dfs(node.left, lvs)
            node.right = dfs(node.right, lvs)
            return node

        result = []
        while root:
            cur_leaves = []
            root = dfs(root, cur_leaves)
            if cur_leaves:
                result.append(cur_leaves)
        return result
