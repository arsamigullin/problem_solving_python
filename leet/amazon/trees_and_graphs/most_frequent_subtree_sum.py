# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
import collections
import  typing
List = typing.List
class Solution:
    def findFrequentTreeSum(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        dsum = collections.defaultdict(int)
        m = 0
        def helper(node):
            nonlocal m
            if not node:
                return 0
            total = node.val + helper(node.left) + helper(node.right)
            dsum[total]+=1
            m = max(m, dsum[total])
            return total
        helper(root)
        return [k for k, v in dsum.items() if v == m]