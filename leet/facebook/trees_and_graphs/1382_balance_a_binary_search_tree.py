# Definition for a binary tree node.
# similar
# bst
# 108. Convert Sorted Array to Binary Search Tree
# 449. Serialize and Deserialize BST
# # 889. Construct Binary Tree from Preorder and Postorder Traversal
# # 106. Construct Binary Tree from Inorder and Postorder Traversal
# # 105. Construct Binary Tree from Preorder and Inorder Traversal

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:

        arr = []

        def dfs(node):
            if not node:
                return
            dfs(node.left)
            arr.append(node.val)
            dfs(node.right)

        dfs(root)

        def construct(lo, hi):
            if lo > hi:
                return None
            mid = (lo + hi) // 2
            node = TreeNode(arr[mid])
            node.left = construct(lo, mid - 1)
            node.right = construct(mid + 1, hi)
            return node

        return construct(0, len(arr) - 1)