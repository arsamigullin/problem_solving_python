# Definition for a binary tree node.
# Similar
# 449. Serialize and Deserialize BST
# # 889. Construct Binary Tree from Preorder and Postorder Traversal
# # 106. Construct Binary Tree from Inorder and Postorder Traversal
# # 105. Construct Binary Tree from Preorder and Inorder Traversal
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

from typing import List


class Solution:
    '''
    let's consider this binary tree
            8
           / \
          5   10
        / \     \
       1   7     12

       since we need to construct binary search tree
       each node has its unique place which is retricted by lo and hi value
       for example for node 7 the lo is 5 and hi is 8
       if the current value preorder[idx] is out of this range
       we return None
    '''
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:

        idx = 0

        def helper(lo=float('-inf'), hi=float('inf')):
            nonlocal idx
            if idx >= len(preorder):
                return None
            val = preorder[idx]
            # once condition of binary search tree is vialated
            # that means we have to stop here since the value under
            # preorder[idx] should be place in other place
            if lo > val or hi < val:
                return None
            idx += 1
            root = TreeNode(val)
            root.left = helper(lo, val)
            root.right = helper(val, hi)
            return root

        return helper()


class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        n = len(preorder)
        if not n:
            return None

        root = TreeNode(preorder[0])
        stack = [root, ]

        for i in range(1, n):
            # take the last element of the stack as a parent
            # and create a child from the next preorder element
            node, child = stack[-1], TreeNode(preorder[i])
            # adjust the parent
            while stack and stack[-1].val < child.val:
                node = stack.pop()

            # follow BST logic to create a parent-child link
            if node.val < child.val:
                node.right = child
            else:
                node.left = child
                # add the child into stack
            stack.append(child)

        return root
