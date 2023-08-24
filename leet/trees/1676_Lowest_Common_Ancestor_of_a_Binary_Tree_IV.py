# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# both are correct. The second is more elegant
class Solution:
    def lowestCommonAncestor1(self, root: 'TreeNode', nodes: 'List[TreeNode]') -> 'TreeNode':

        print(nodes[0] or nodes[1])
        res = None
        vals = set([node.val for node in nodes])

        def helper(node):
            nonlocal res
            if node is None:
                return False
            l = helper(node.left)
            r = helper(node.right)
            cur = node.val in vals
            if cur:
                vals.discard(node.val)
            exist = (l & r) or (l & cur) or (r & cur)
            if exist and len(vals) == 0:
                res = node
            if len(vals) == 0 and res is None:
                res = node
            return l or r or cur

        helper(root)
        return res

    def lowestCommonAncestor(self, root: 'TreeNode', nodes: 'List[TreeNode]') -> 'TreeNode':
        nodes = set(nodes)
        return self.dfs(root, nodes)

    def dfs(self, root, nodes):
        if not root:
            return 0
        # even though below the root we have nodes from nodes array it does not matter
        if root in nodes:
            return root
        l = self.dfs(root.left, nodes)
        r = self.dfs(root.right, nodes)
        if l and r:
            return root
        return l or r