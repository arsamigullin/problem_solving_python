# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def splitBST(self, root: TreeNode, V: int) -> List[TreeNode]:

        def dfs(node):
            if not node:
                return None, None
            # since we go to the right subtree from smaller node
            # (the node which is smaller than V)
            # there fore we must update its right branch with the tree that is smallest or equal V
            if V >= node.val:
                small, large = dfs(node.right)
                node.right = small
                return node, large
            else:
                small, large = dfs(node.left)
                node.left = large
                return small, node

        return dfs(root)