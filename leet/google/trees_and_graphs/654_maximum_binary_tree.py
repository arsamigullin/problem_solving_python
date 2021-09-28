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
            # since every root of subtree is going to be a max val
            # we extract all that less than cur.val
            # the latest item in stack is the left one
            while stack and stack[-1].val < cur.val:
                # it is possible to rewrite cur.left multiple times
                cur.left = stack.pop()
            if stack:
                # it is possible to rewerite multiple times
                # [3,2,1,6,0,5], we have 6.right = 0 and the 6.right = 5
                stack[-1].right = cur
            stack.append(cur)
        return stack[0]


if __name__ == '__main__':
    s = Solution()
    s.constructMaximumBinaryTree([3,2,1,6,0,5])