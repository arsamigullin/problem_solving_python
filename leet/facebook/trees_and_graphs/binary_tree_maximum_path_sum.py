
# this algo uses PostOrder traversal
# at the root node we check if current sum of tree (made of current node being a root and its left and right children)
# has maximum value by updating global max_sum variable
# But since we look for path we must return node.val + max(node.left.val, node.right.val)
# let's consider the tree
#         -5
#         /\
#       -1 -6
#       /\
#     -2  -3
# First we will see if -1 +

class Solution:
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        def max_gain(node):
            nonlocal max_sum
            if not node:
                return 0

            # we compare here with 0 because if node and node.left are negative
            # their sum will move away from maximum value
            # there fore we does not count the negative numbers
            # and current node will have max val
            left_gain = max(max_gain(node.left), 0)
            right_gain = max(max_gain(node.right), 0)

            # obtain max val from current tree
            price_newpath = node.val + left_gain + right_gain

            # check if the current tree has max val
            max_sum = max(max_sum, price_newpath)

            # since we look for path (NOT Tree) we cannot return sum of tree
            # we have to return sum of path
            return node.val + max(left_gain, right_gain)

        max_sum = float('-inf')
        max_gain(root)
        return max_sum


class Solution:
    def maxPathSum(self, root) -> int:
        max_val = float('-inf')

        def dfs(node):
            nonlocal max_val
            if not node:
                return float('-inf')
            max_val = max(max_val, node.val)
            l = dfs(node.left)
            r = dfs(node.right)
            max_val = max(max_val, l + node.val)
            max_val = max(max_val, r + node.val)
            max_val = max(max_val, l + node.val + r)
            return max(node.val + r, node.val + l, node.val)

        dfs(root)
        return max_val