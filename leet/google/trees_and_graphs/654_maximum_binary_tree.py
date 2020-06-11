# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution1:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        if not nums:
            return None
        d={v:i for i, v in enumerate(nums)}
        def dfs(lo, hi):
            if lo==hi:
                return None
            val = max(nums[lo:hi])
            root = TreeNode(val)
            root.left = dfs(lo, d[val])
            root.right = dfs(d[val]+1, hi)
            return root
        return dfs(0, len(nums))

class Solution(object):
    def constructMaximumBinaryTree(self, arr):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        stack = []
        for num in arr:
            cur = TreeNode(num)
            while stack and stack[-1].val < cur.val:
                cur.left = stack.pop()
            if stack:
                stack[-1].right = cur
            stack.append(cur)
        return stack[0]


if __name__ == '__main__':
    s = Solution()
    s.constructMaximumBinaryTree([3,2,1,6,0,5])