# Definition for a binary tree node.
# similar
# bst
# 1382. Balance a Binary Search Tree
# 108. Convert Sorted Array to Binary Search Tree
# 449. Serialize and Deserialize BST
# # 889. Construct Binary Tree from Preorder and Postorder Traversal
# # 106. Construct Binary Tree from Inorder and Postorder Traversal
# # 105. Construct Binary Tree from Preorder and Inorder Traversal
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
import typing
List = typing.List
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        def helper(left, right):
            if left > right:
                return None

            # always choose left middle node as a root
            p = (left + right) // 2

            # inorder traversal: left -> node -> right
            root = TreeNode(nums[p])
            # left is going to be between left and p - 1
            root.left = helper(left, p - 1)
            # right is going to be between p+1 and right
            root.right = helper(p + 1, right)
            return root

        return helper(0, len(nums) - 1)

if __name__ == "__main__":
    s = Solution()
    s.sortedArrayToBST([1,2,3,4,5,6,7,8,9])