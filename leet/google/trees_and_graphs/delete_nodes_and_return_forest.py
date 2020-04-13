# Definition for a binary tree node.

import typing
List = typing.List

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# this problem
# https://leetcode.com/problems/delete-nodes-and-return-forest/
class Solution:
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        res = []
        if not root:
            return res
        if not to_delete:
            return root
        # this will speed up the search
        to_delete = set(to_delete)
        # helper return bool val
        # True - this node needs to be deleted from its parent
        def helper(node):
            if not node:
                return False
            if helper(node.left):
                node.left = None
            if helper(node.right):
                node.right = None

            to_del = node.val in to_delete
            # if current node is to be deleted
            if to_del:
                # its left node will compose forest
                if node.left:
                    res.append(node.left)
                # and its right node will compose forest
                if node.right:
                    res.append(node.right)
            return to_del
        # if root will not be deleted we add it to the result list
        if not helper(root):
            res.append(root)
        return res
