# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
import collections
import math
from typing import Optional, List


class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        d = collections.defaultdict(list)
        # these two variables to avoid sorting
        min_col = math.inf
        max_col = -math.inf
        q = collections.deque([(root, 0)])
        while q:
            node, level = q.popleft()
            min_col = min(min_col, level)
            max_col = max(max_col, level)
            d[level].append(node.val)
            if node.left:
                q.append((node.left, level - 1))
            if node.right:
                q.append((node.right, level + 1))

        return [d[key] for key in range(min_col, max_col + 1)]


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        d = collections.defaultdict(list)
        # these two variables to avoid sorting
        min_col = math.inf
        max_col = -math.inf

        def dfs(node, row, col):
            nonlocal min_col, max_col
            if not node:
                return
            min_col = min(min_col, col)
            max_col = max(max_col, col)
            d[col].append((row, node.val))
            dfs(node.left, row + 1, col - 1)
            dfs(node.right, row + 1, col + 1)

        dfs(root, 0, 0)
        res = []

        for col in range(min_col, max_col + 1):
            res.append([val for _, val in sorted(d[col], key=lambda x: x[0])]) # sort only by row here

        return res
