# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    '''
    Note: right most element in the tree is max element
    That is why we start traversing from the right
    so, it will be guaranteed that the node before will have value less than sum
    '''
    def bstToGst(self, root: TreeNode) -> TreeNode:
        tot = 0
        def dfs(node):
            nonlocal tot
            if not node:
                return
            dfs(node.left)
            tot+=node.val
            node.val = tot
            dfs(node.right)
        dfs(root)
        return root