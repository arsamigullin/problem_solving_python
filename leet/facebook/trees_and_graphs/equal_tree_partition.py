# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# thsi problem
# https://leetcode.com/problems/equal-tree-partition/
# 663. Equal Tree Partition
class Solution(object):
    '''
    we store sum of each subtree and then just see if total/2 in seen array

    '''
    def checkEqualTree(self, root):
        seen = []
        def dfs(node):
            if not node:
                return 0
            seen.append(node.val + dfs(node.left) + dfs(node.right))
            return seen[-1]

        total = dfs(root)
        seen.pop()
        return total/2 in seen

