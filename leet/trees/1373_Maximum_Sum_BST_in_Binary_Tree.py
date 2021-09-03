# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

import math
from typing import Optional

# Q: why do we need to return three values
# A: because we do not know from which subtree (left or right) the values are returned
# if returned from left, then to check the BST property we will use the max_left
# if returned from right, then to check the BST property we will the min_right



class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:

        result = - math.inf

        def helper(node):
            nonlocal result
            if not node:
                return 0, math.inf, -math.inf
            l_res, l_min, l_max = helper(node.left)
            r_res, r_min, r_max = helper(node.right)
            # to verify the BST property
            # we use the max from the left subtree and min from the right subtree
            if l_max < node.val < r_min:
                result = max(result, l_res + r_res + node.val)
                # but NOTE, since this will be returned from left or right subtree
                # we want to get the min and max vals
                return l_res + r_res + node.val, min(l_min, node.val), max(r_max, node.val)
            else:
                return 0, -math.inf, math.inf

        return max(helper(root)[0], result)