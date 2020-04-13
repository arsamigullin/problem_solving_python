# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    '''
    Important! this is BST
    So, we do not need to visit every node in tree
    
    '''
    def closestValue(self, root: TreeNode, target: float) -> int:
        def helper(node):
            if not node:
                return (0, float('inf'))
            
            if target < node.val:
                res = helper(node.left)
            else:
                res = helper(node.right)
            dif = abs(node.val - target)
            if dif < res[1]:
                return (node.val, dif)
            else:
                return res

        return helper(root)[0]