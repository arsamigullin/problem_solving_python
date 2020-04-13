# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
import collections
import typing
List = typing.List

class SolutionMy:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        q = collections.deque([(root, 0)])
        res = []
        while q:
            node, level = q.popleft()
            if level + 1 == len(res):
                res[level].append(node.val)
            else:
                res.append([node.val])
            if node.left:
                q.append((node.left, level + 1))
            if node.right:
                q.append((node.right, level + 1))
        return res


class Solution:
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        levels = []
        if not root:
            return levels

        def helper(node, level):
            # start the current level
            if len(levels) == level:
                levels.append([])

            # append the current node value
            levels[level].append(node.val)

            # process child nodes for the next level
            if node.left:
                helper(node.left, level + 1)
            if node.right:
                helper(node.right, level + 1)

        helper(root, 0)
        return levels