# Definition for a binary tree node.

# similar 241
# 894

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



class Solution:
    def generateTrees(self, n: int):

        memo = {}

        def helper(lo, hi):
            if lo > hi:
                return [None]
            if (lo, hi) not in memo:
                ans = []
                # How values of nodes are alternating?
                # let's say lo is 2 and hi is 3
                # 1 iteration, i = 2
                # lo is 2 and i-1 is 1, so the 2  loop returns [None]
                # i+1 is 3, i.e. i+1 == hi, so it will fall to the 3rd loop and return [TreeNode(3)]
                # so after first iteration with i = 2 (which is root of subtree) ans contains [TreeNode(3)]
                # 2 iteration i = 3
                # lo is still 2 and i-1 is 2!!!!, it will fall into the 2nd loop and return [TreeNode(2)]
                # i+1 > hi, i.e. 4>3 so it returns None

                # after two iterations, the ans = [TreeNode(2), TreeNode(3)]
                for i in range(lo, hi + 1):
                    for left in helper(lo, i - 1): # 2 loop
                        for right in helper(i + 1, hi): # 3 loop
                            root = TreeNode(i)
                            root.left = left
                            root.right = right
                            ans.append(root)
                memo[(lo, hi)] = ans
            return memo[(lo, hi)]

        return helper(1, n)

if __name__ == '__main__':
    s = Solution()
    s.generateTrees(3)