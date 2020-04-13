# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
# this problem
class Solution:
    '''
    The key point here is once we've determined difference greater that 1
    we return everything immediately
    '''
    def isBalanced(self, root: TreeNode) -> bool:
        def helper(node):
            if not node:
                return (0, True)
            ll, lres = helper(node.left)
            rl, rres = helper(node.right)
            ll += 1
            rl += 1
            if lres and rres:
                if abs(ll - rl) <= 1:
                    return (max(ll, rl), True)
                else:
                    return (-1, False)
            else:
                return (-1, False)
        return helper(root)[1]
