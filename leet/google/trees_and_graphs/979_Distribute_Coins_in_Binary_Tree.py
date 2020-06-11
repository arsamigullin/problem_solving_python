class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def distributeCoins(self, root):
        self.ans = 0

        # we need to use dfs
        # doing that way it will balances the coins
        def dfs(node):
            if not node: return 0
            L, R = dfs(node.left), dfs(node.right)
            self.ans += abs(L) + abs(R)
            return node.val + L + R - 1

        dfs(root)
        return self.ans

if __name__ == '__main__':
    #[0, 2, 3, 0, 0, None, None, 1]
    root = TreeNode(0)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(0)
    root.left.right = TreeNode(0)
    root.left.left.left = TreeNode(1)

    s = Solution()
    s.distributeCoins(root)
