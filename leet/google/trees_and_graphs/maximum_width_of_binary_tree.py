# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
import collections
class SolutionMy:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        if not root:
            return 0
        prev_level = -1
        width = 0
        cur_max = 0
        cur_min = 0
        q = collections.deque([(root, 0, 0)])
        while q:
            node, level, ind = q.popleft()
            if level != prev_level:
                width = max(width, cur_max - cur_min)
                cur_max = float('-inf')
                cur_min = float('inf')
                prev_level = level
            cur_max = max(cur_max, ind)
            cur_min = min(cur_min, ind)
            if node.left:
                q.append((node.left, level + 1, 2 * ind))
            if node.right:
                q.append((node.right, level + 1, 2 * ind + 1))

        return max(width, cur_max - cur_min) + 1


class SolutionBFS:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        q = collections.deque([(root, 0, 0)])
        prev_lev = ans = veryleft = 0

        while q:

            node, level, pos = q.popleft()
            if node:
                if prev_lev != level:
                    veryleft = pos
                    prev_lev = level
                ans = max(ans, pos - veryleft + 1)
                if node.left:
                    q.append((node.left, level + 1, 2 * pos))
                if node.right:
                    q.append((node.right, level + 1, 2 * pos + 1))
        return ans

class Solution(object):
    def widthOfBinaryTree(self, root):
        self.ans = 0
        left = {}
        def dfs(node, depth = 0, pos = 0):
            if node:
                left.setdefault(depth, pos)
                self.ans = max(self.ans, pos - left[depth] + 1)
                dfs(node.left, depth + 1, pos * 2)
                dfs(node.right, depth + 1, pos * 2 + 1)

        dfs(root)
        return self.ans
