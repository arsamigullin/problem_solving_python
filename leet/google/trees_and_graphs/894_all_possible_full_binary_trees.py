# Definition for a binary tree node.
# similar 241
# similar 95. Unique Binary Search Trees II
# dynamic programming
# divide and conquer
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# FAQ
# What ensures the node either has 2 nodes or 0 nodes?
# this construction, because assignment left and right happens inside of innermost loop
#for left in self.allPossibleFBT(x):
#    for right in self.allPossibleFBT(y):



class Solution:
    memo = {0: [], 1: [TreeNode(0)]}

    def allPossibleFBT(self, N: int) -> List[TreeNode]:
        if N not in Solution.memo:
            ans = []
            for x in range(N):
                y = N - x - 1 # here 1 is for root
                for left in self.allPossibleFBT(x):
                    for right in self.allPossibleFBT(y):
                        root = TreeNode(0)
                        root.left = left
                        root.right = right
                        ans.append(root)
            Solution.memo[N] = ans

        return Solution.memo[N]

# the same as above but
class Solution1:
    def allPossibleFBT(self, n: int):

        memo = {0: [], 1: [TreeNode(0)]}

        def helper(n):
            if n not in memo:
                ans = []
                for x in range(n):
                    y = n - x - 1  # here 1 is for root
                    for left in helper(x):
                        for right in helper(y):
                            root = TreeNode(0)
                            root.left = left
                            root.right = right
                            ans.append(root)
                memo[n] = ans
            return memo[n]

        return helper(n)

if __name__ == '__main__':
    s = Solution1()
    s.allPossibleFBT(7)