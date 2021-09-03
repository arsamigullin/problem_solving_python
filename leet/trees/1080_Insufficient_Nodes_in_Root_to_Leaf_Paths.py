class Solution1(object):
    def sufficientSubset(self, root, limit):
        """
        :type root: TreeNode
        :type limit: int
        :rtype: TreeNode
        """

        def dfs(node, tot):
            if not node:
                return None, True
            if not (node.left or node.right):
                tot = tot + node.val
                return (None if tot < limit else node, tot < limit)
            node.left, l = dfs(node.left, tot + node.val)
            node.right, r = dfs(node.right, tot + node.val)
            return (None, True) if l and r else (node, False)

        return dfs(root, 0)[0]


class Solution:
    def sufficientSubset(self, root, limit, pathSum=0):
        if not root: return None
        if not root.left and not root.right:
            if pathSum + root.val < limit:
                return None
            return root
        root.left = self.sufficientSubset(root.left, limit, pathSum + root.val)
        root.right = self.sufficientSubset(root.right, limit, pathSum + root.val)
        if not root.left and not root.right:
            return None
        return root