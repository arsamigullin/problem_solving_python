# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
import collections


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findClosestLeaf(self, root: TreeNode, k: int) -> int:
        graph = collections.defaultdict(list)
        q = collections.deque([root])
        leaves = []
        while q:
            node = q.popleft()
            graph[node.val]
            if not node.left and not node.right:
                leaves.append(node.val)
            else:
                if node.left:
                    graph[node.val].append(node.left.val)
                    graph[node.left.val].append(node.val)
                    q.append(node.left)
                if node.right:
                    graph[node.val].append(node.right.val)
                    graph[node.right.val].append(node.val)
                    q.append(node.right)

        visited = set()
        visited.add(k)
        graph[root.val].append(root.val)
        q = collections.deque([k])
        # since dfs finds the shorter distance
        # we will start from k and first leaf is the answer
        while q:
            node = q.popleft()
            if node:
                if len(graph[node]) <= 1:
                    return node
                for child in graph[node]:
                    if child not in visited:
                        visited.add(child)
                        q.append(child)

        return root.val


class Solution:
    def findClosestLeaf(self, root: TreeNode, k: int) -> int:
        graph = collections.defaultdict(set)
        q = collections.deque([root])
        leaves = []
        while q:
            node = q.popleft()
            graph[node.val]
            if not node.left and not node.right:
                leaves.append(node.val)
            else:
                if node.left:
                    graph[node.val].add(node.left.val)
                    graph[node.left.val].add(node.val)
                    q.append(node.left)
                if node.right:
                    graph[node.val].add(node.right.val)
                    graph[node.right.val].add(node.val)
                    q.append(node.right)
        length = float('inf')
        nd = -1
        # print(leaves, graph)
        for leaf in leaves:
            visited = set()
            q = collections.deque([(leaf, 0, leaf)])
            while q:
                node, l, lf = q.popleft()
                if node == k:
                    if l < length:
                        nd = lf
                        length = l
                        # print(nd)
                    break
                if node in visited:
                    continue
                visited.add(node)
                for child in graph[node]:
                    if child not in visited:
                        q.append((child, l + 1, lf))
        return nd
