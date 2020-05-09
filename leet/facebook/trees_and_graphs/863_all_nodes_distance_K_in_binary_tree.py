# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
import collections


class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, K: int) -> List[int]:
        graph = collections.defaultdict(list)

        def dfs(node, parent):
            if not node:
                return
            if parent is not None:
                graph[node.val].append(parent)
            if node.left:
                graph[node.val].append(node.left.val)
                dfs(node.left, node.val)
            if node.right:
                graph[node.val].append(node.right.val)
                dfs(node.right, node.val)

        dfs(root, None)
        visited = set()
        res = []
        q = collections.deque([(target.val, 0)])
        while q:
            node, level = q.popleft()
            if node in visited:
                continue
            visited.add(node)
            if level == K:
                res.append(node)
            elif level < K:
                for child in graph[node]:
                    if child not in visited:
                        q.append((child, level + 1))
        return res