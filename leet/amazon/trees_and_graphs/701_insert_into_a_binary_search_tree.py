class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:

        def insert(val, node):
            if not node:
                return
            if node.val < val:
                if node.right is None:
                    node.right = TreeNode(val)
                else:
                    insert(val, node.right)
            else:
                if node.left is None:
                    node.left = TreeNode(val)
                else:
                    insert(val, node.left)

        insert(val, root)
        return root


class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:

        node = root
        while node:
            if node.val < val:
                if node.right is None:
                    node.right = TreeNode(val)
                    break
                else:
                    node = node.right
            else:
                if node.left is None:
                    node.left = TreeNode(val)
                    break
                else:
                    node = node.left
        return root