# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# this problem
# https://leetcode.com/problems/deepest-leaves-sum/

import collections
class SolutionMy:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        prev_level = ans = 0
        q = collections.deque([(root, 0)])
        while q:
            node, level = q.popleft()
            if node:
                if level != prev_level:
                    ans = 0
                    prev_level = level
                ans += node.val
                if node.left:
                    q.append((node.left, level + 1))
                if node.right:
                    q.append((node.right, level + 1))
        return ans


class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        deepest_sum = depth = 0
        stack = [(root, 0)]

        while stack:
            node, curr_depth = stack.pop()
            if node.left is None and node.right is None:
                # if this leaf is the deepest one seen so far
                if depth < curr_depth:
                    deepest_sum = node.val  # start new sum
                    depth = curr_depth  # note new depth
                # if there were already leaves at this depth
                elif depth == curr_depth:
                    deepest_sum += node.val  # update existing sum

            else:
                if node.right:
                    stack.append((node.right, curr_depth + 1))
                if node.left:
                    stack.append((node.left, curr_depth + 1))

        return deepest_sum