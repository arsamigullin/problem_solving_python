# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def twoSumBSTs(self, root1: TreeNode, root2: TreeNode, target: int) -> bool:
        A = set()

        def dfs(node):
            if not node:
                return
            dfs(node.left)
            A.add(node.val)
            dfs(node.right)

        dfs(root1)

        stack = []
        node = root2
        while stack or node:
            if node:
                stack.append(node)
                node = node.left
            else:
                nd = stack.pop()
                if target - nd.val in A:
                    return True
                node = nd.right
        return False