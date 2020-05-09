# Definition for a binary tree node.
import collections
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        d = collections.defaultdict(dict)
        q = collections.deque([[root, 0, 0]])
        while q:
            node, lvl, depth = q.popleft()
            d[lvl].setdefault(depth, []).append(node.val)
            if node.left:
                q.append([node.left, lvl - 1, depth + 1])
            if node.right:
                q.append([node.right, lvl + 1, depth + 1])

        res = []
        for k in sorted(d.keys()):
            data = []
            for ki in sorted(d[k]):
                data += sorted(d[k][ki])
            res.append(data)
        return res
