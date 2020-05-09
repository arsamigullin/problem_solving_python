# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    '''
    we return min and max from each subtree
    and then to find the result we do abs substration from each min and max of each sub tree

    '''
    def maxAncestorDiff(self, root: TreeNode) -> int:
        res = 0

        def findMinMax(node, parentval):
            nonlocal res
            if not node:
                return parentval, parentval
            lmin, lmax = findMinMax(node.left, node.val)
            rmin, rmax = findMinMax(node.right, node.val)
            res = max(res, abs(node.val - lmin), abs(node.val - lmax), abs(node.val - rmin), abs(node.val - rmax))
            return min(node.val, lmin, rmin), max(node.val, lmax, rmax)

        lmin, lmax = findMinMax(root.left, root.val)
        rmin, rmax = findMinMax(root.right, root.val)

        return max(res, abs(root.val - lmin), abs(root.val - lmax), abs(root.val - rmin), abs(root.val - rmax))