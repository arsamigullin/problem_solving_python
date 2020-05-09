# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidSequence(self, root: TreeNode, arr: List[int]) -> bool:

        def dfs(node, i):
            if node is None:
                return False
            if i == len(arr):
                return False
            if node.val == arr[i]:
                if node.left is None and node.right is None:
                    return i == len(arr) - 1
                elif node.left and node.right:
                    return dfs(node.left, i + 1) or dfs(node.right, i + 1)
                elif node.left:
                    return dfs(node.left, i + 1)
                else:
                    return dfs(node.right, i + 1)
            return False

        return dfs(root, 0)