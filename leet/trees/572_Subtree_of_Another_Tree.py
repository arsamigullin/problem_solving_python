# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:

        def the_same(node, subnode):
            if not (node or subnode):
                return True
            elif not (node and subnode):
                return False
            return node.val == subnode.val and the_same(node.left, subnode.left) and the_same(node.right, subnode.right)

        def dfs(node):
            if not node:
                return False
            if the_same(node, t):
                return True
            return dfs(node.left) or dfs(node.right)

        return dfs(s)

# O(n+m), however adding values can potentially increase time complexity
class Solution:

    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        def get_tree(node):
            if not node:
                return None
            return f"# {node.val} {get_tree(node.left)} {get_tree(node.right)}"

        return get_tree(t) in get_tree(s)
