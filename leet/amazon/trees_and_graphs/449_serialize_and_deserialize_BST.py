# Definition for a binary tree node.

# 449
# 889. Construct Binary Tree from Preorder and Postorder Traversal

# similar
# 106. Construct Binary Tree from Inorder and Postorder Traversal
# 105. Construct Binary Tree from Preorder and Inorder Traversal

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.
        """
        preorder = []

        def helper(node):
            if node:
                preorder.append(str(node.val))
                helper(node.left)
                helper(node.right)

        helper(root)
        return '|'.join(preorder)

    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.
        """
        if not data:
            return None
        preorder = list(map(int, data.split('|')))

        i = 0

        def helper(lo=float('-inf'), hi=float('inf')):
            nonlocal i
            if i >= len(preorder):
                return None
            val = preorder[i]
            if val < lo or val > hi:
                return None
            i += 1
            root = TreeNode(val)
            root.left = helper(lo, val)
            root.right = helper(val, hi)
            return root

        return helper()


class Codec:
    def serialize(self, root):
        """
        Encodes a tree to a single string.
        """

        def postorder(root):
            return postorder(root.left) + postorder(root.right) + [root.val] if root else []

        return ' '.join(map(str, postorder(root)))

    def deserialize(self, data):
        """
        Decodes your encoded data to tree.
        """

        def helper(lower=float('-inf'), upper=float('inf')):
            if not data or data[-1] < lower or data[-1] > upper:
                return None

            val = data.pop()
            root = TreeNode(val)
            root.right = helper(val, upper)
            root.left = helper(lower, val)
            return root

        data = [int(x) for x in data.split(' ') if x]
        return helper()


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.
        """

        def int_to_str(num):
            sb = [chr(num >> (i * 8) & 0xff) for i in range(4)]
            sb.reverse()
            return ''.join(sb)

        preorder = []

        def helper(node):
            if node:
                preorder.append(int_to_str(node.val))
                helper(node.left)
                helper(node.right)

        helper(root)
        return ''.join(preorder)

    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.
        """

        def str_to_int(val):
            res = 0
            for ch in val:
                res = res * 256 + ord(ch)
            return res

        if not data:
            return None

        start, end = 0, 4

        def helper(lo=float('-inf'), hi=float('inf')):
            nonlocal start, end
            if start >= len(data):
                return None
            val = str_to_int(data[start:end])
            if val < lo or val > hi:
                return None
            start += 4
            end += 4
            root = TreeNode(val)
            root.left = helper(lo, val)
            root.right = helper(val, hi)
            return root

        return helper()


class Codec1:

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
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        print(data)
        if not data:
            return
        preorder = data.split('|')
        i = 0

        def helper():
            nonlocal i
            if preorder[i] == '#':
                return None
            node = TreeNode(int(preorder[i]))
            i += 1
            node.left = helper()
            i += 1
            node.right = helper()
            return node

        return helper()

if __name__ == '__main__':
    c = Codec1()
    c.deserialize()