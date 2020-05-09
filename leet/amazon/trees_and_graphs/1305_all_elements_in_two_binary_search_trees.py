# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        A = []
        def dfs(node1, node2):
            if not node1 and not node2:
                return
            if node1:
                A.append(node1.val)
            if node2:
                A.append(node2.val)
            dfs(node1.left if node1 and node1.left else None, node2.left if node2 and node2.left else None)
            dfs(node1.right if node1 and node1.right else None, node2.right if node2 and node2.right else None)
        dfs(root1, root2)
        A.sort()
        return A