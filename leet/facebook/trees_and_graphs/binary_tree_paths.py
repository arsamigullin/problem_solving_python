class Solution:
    def binaryTreePaths(self, root):
        res = []
        def findPaths(node, path):
            if node is None:
                return
            if path == "":
                path = str(node.val)
            else:
                path+="->" + str(node.val)
            if node.left is None and node.right is None:
                res.append(path)
                return
            findPaths(node.left, path)
            findPaths(node.right, path)
        findPaths(root, "")
        return res