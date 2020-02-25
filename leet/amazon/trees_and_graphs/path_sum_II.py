# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        if not root:
            return []
        res = []
        def find(node, s, nodes):
            if not node:
                return 
            nodes.append(node.val)
            if s - node.val == 0 and node.left is None and node.right is None:
                res.append(nodes[:])
            else:
                find(node.left, s - node.val, nodes)
                find(node.right, s - node.val, nodes)
            nodes.pop()
        find(root, sum, [])
        return res