import math


class Solution:
    def __init__(self):
        self.prev = None

    # according to Cormen (p.287) Inorder traversal prints out the values of nodes in sorted order
    def isValidBST(self, root):
        if root is None:
            return True
        is_left = root.left is None or self.isValidBST(root.left)
        # check if the latest value is greater than current
        if self.prev is not None and self.prev >= root.val:
            return False
        self.prev = root.val
        is_right = root.right is None or self.isValidBST(root.right)
        return is_left and is_right

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:

        def validate(node, low=-math.inf, high=math.inf):
            # Empty trees are valid BSTs.
            if not node:
                return True
            # The current node's value must be between low and high.
            if node.val <= low or node.val >= high:
                return False

            # The left and right subtree must also be valid.
            return (validate(node.left, low, node.val) and validate(node.right, node.val, high))

        return validate(root)