# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ""
        preorder = []
        def helper(node):
            if not node:
                preorder.append('#')
                return
            preorder.append(str(node.val))
            helper(node.left)
            helper(node.right)
        helper(root)
        return '|'.join(preorder)

    def deserialize(self, data):
        if not data:
            return
        preorder = data.split('|')
        i = 0
        def helper():
            nonlocal i
            if preorder[i] == '#':
                return None
            node = TreeNode(int(preorder[i]))
            i+=1
            node.left = helper()
            i+=1
            node.right = helper()
            return node

        return helper()
