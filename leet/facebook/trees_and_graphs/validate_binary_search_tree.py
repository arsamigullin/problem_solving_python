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