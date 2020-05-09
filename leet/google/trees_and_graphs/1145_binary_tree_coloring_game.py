# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def btreeGameWinningMove(self, root: TreeNode, n: int, x: int) -> bool:
        left, right = 0, 0

        # we want to count nodes in left and right subtrees of x node
        def dfs(node, cnt):
            nonlocal left, right
            if not node:
                return 0
            if node.val == x:
                dfs(node.left, 1)
                dfs(node.right, 2)
            else:
                if cnt == 1:
                    left += 1
                if cnt == 2:
                    right += 1
                dfs(node.left, cnt)
                dfs(node.right, cnt)

        dfs(root, False)
        # we also want to count how many nodes right above x node
        top = n - (left + right) - 1
        # player 2 will take move in the subtree with max node count
        m = max(top, left, right)
        # and after player 2 takes move the count nodes for second player
        # is greater than count of nodes for the first player
        # that mean player2 will win
        return m - 1 > (top + left + right) - m
