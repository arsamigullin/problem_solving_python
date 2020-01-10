# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
# Observations
# to understand what are the deepest leaves
# it is not necessary to find the depth of the tree
# we start count depth from the leaves
# and then check to see which depth is greater left or right
# along we the depth we also return lca
class Solution:

    def lcaDeepestLeaves(self, root: TreeNode) -> TreeNode:
        def rca(node):
            if node is None:
                return (None, -1)
            l, dl = rca(node.left)
            r, dr = rca(node.right)
            if dl > dr:
                return  l, dl + 1,
            if dl < dr:
                return  r, dr + 1
            return node, dl + 1

        return rca(root)[0]