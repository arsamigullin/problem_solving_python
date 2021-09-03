import collections
from _ast import List
from typing import Optional


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def boundaryOfBinaryTree(self, root: Optional[TreeNode]) -> List[int]:

        if not root:
            return []

        if not (root.left or root.right):
            return [root.val]

        node = root.left
        result = [root.val]
        stack = [node]

        # add lef most non-leaf nodes
        while node:
            if node.left or node.right:
                result.append(node.val)
            if node.left:
                node = node.left
            else:
                node = node.right

        def add_leaves(node):
            if not node:
                return
            if not (node.left or node.right):
                result.append(node.val)
            add_leaves(node.left)
            add_leaves(node.right)

        # add leaves
        add_leaves(root)

        # add right most non-leaf nodes
        queue = collections.deque()
        node = root.right
        while node:
            if node.left or node.right:
                queue.appendleft(node.val)
            if node.right:
                node = node.right
            else:
                node = node.left

        return result + list(queue)


class Solution:
    def boundaryOfBinaryTree(self, root):

        if not root:
            return []
        if not (root.left or root.right):
            return [root.val]

        node_dict = collections.defaultdict(list)

        q = collections.deque([(root, 0)])
        while q:
            node, level = q.popleft()
            # if node.left or node.right:
            node_dict[level].append(node.val)
            if node.left:
                q.append((node.left, level + 1))
            if node.right:
                q.append((node.right, level + 1))

        result = [root.val]

        def dfs_left(node):
            if not node:
                return
            if not (node.left or node.right):
                return
            result.append(node.val)
            if node.left:
                dfs_left(node.left)
            else:
                dfs_left(node.right)

        def dfs_right(node):
            if not node:
                return
            if not (node.left or node.right):
                return
            if node.right:
                dfs_right(node.right)
            else:
                dfs_right(node.left)
            result.append(node.val)

        def add_leaves(node):
            if not node:
                return
            if not (node.left or node.right):
                result.append(node.val)
                return
            add_leaves(node.left)
            add_leaves(node.right)

        dfs_left(root.left)
        add_leaves(root)
        dfs_right(root.right)

        return result





