class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    '''
    if node within the range we must visit both children
    if node less that L, no need to visit left node since left node is less that parent, so we go to the right node
    if node is greater R, no need to visit right node since right node is greater than parent, so we go to the left noe
    '''
    def trimBST(self, root: TreeNode, L: int, R: int) -> TreeNode:
        def dfs(node):
            if not node:
                return None
            if L <= node.val <= R:
                node.left = dfs(node.left)
                node.right = dfs(node.right)
                return node
            elif node.val < L:
                return dfs(node.right)
            else:
                return dfs(node.left)

        return dfs(root)