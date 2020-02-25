# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        
        def find(node, s):
            if node is None:
                return False
            if node.val + s == sum and node.left is None and node.right is None:
                return True
            else:
                return find(node.left, s + node.val) or find(node.right, s + node.val) 
        return find(root, 0)
                