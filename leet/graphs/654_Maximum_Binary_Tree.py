# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums):
        n = len(nums)

        def helper(lo, hi):
            if lo >= hi:
                return None
            arr = nums[lo:hi]
            root_val = max(arr)
            i = arr.index(root_val)
            root = TreeNode(root_val)
            root.left = helper(lo, i)
            root.right = helper(i + 1, hi)
            return root

        return helper(0, len(nums))

if __name__ == '__main__':
    s = Solution()
    s.constructMaximumBinaryTree([3,2,1,6,0,5])