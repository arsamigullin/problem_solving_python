# Definition for a binary tree node.
# this problem
# https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

import collections
import typing
List = typing.List
class MySolution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:

        if not root:
            return []
        LEFT, RIGHT = 0, 1
        q = collections.deque([(root, LEFT, 0)])

        res = []
        while q:
            node, direction, level = q.popleft()
            if len(res) == level + 1:
                if direction == RIGHT:
                    res[level].appendleft(node.val)
                else:
                    res[level].append(node.val)
            else:
                collection = collections.deque([node.val])
                res.append(collection)
            if node.left:
                q.append((node.left, direction ^ 1, level + 1))
            if node.right:
                q.append((node.right, direction ^ 1, level + 1))
        return res


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque

class Solution:
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        ret = []
        level_list = deque()
        if root is None:
            return []
        # start with the level 0 with a delimiter
        node_queue = deque([root, None])
        is_order_left = True

        while len(node_queue) > 0:
            curr_node = node_queue.popleft()

            if curr_node:
                if is_order_left:
                    level_list.append(curr_node.val)
                else:
                    level_list.appendleft(curr_node.val)

                if curr_node.left:
                    node_queue.append(curr_node.left)
                if curr_node.right:
                    node_queue.append(curr_node.right)
            else:
                # we finish one level
                ret.append(level_list)
                # add a delimiter to mark the level
                if len(node_queue) > 0:
                    node_queue.append(None)

                # prepare for the next level
                level_list = deque()
                is_order_left = not is_order_left

        return ret