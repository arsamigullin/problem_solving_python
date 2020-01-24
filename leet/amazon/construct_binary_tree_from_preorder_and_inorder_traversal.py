# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
import collections

# Observations
# Inorder traversal splits the the array on two halves
# for example
# inorder [9,3,15,20,7],
# preorder [9,15,7,20,3]. The root is 3
# 3 splits inorder on two halves
# before start we mapping inorder to the dict where key is val and value is index
# On each iteration we poppingLEFT from postorder and create a root
# IMPORTANT
# since in the preorder the left nodes comes close to the root (1)
# we start form the node from its LEFT child
class Solution:
    def buildTree(self, preorder: list, inorder: list) -> TreeNode:
        preorderq = collections.deque(preorder)
        d = {v: i for i, v in enumerate(inorder)}
        def helper(in_left, in_right):
            if in_left > in_right:
                return None
            val = preorderq.popleft()
            node = TreeNode(val)
            index = d[val]
            node.left = helper(in_left, index - 1)
            node.right = helper(index + 1, in_right)
            return node

        return helper(0, len(preorder) - 1)


if __name__ == "__main__":
    s = Solution()
    s.buildTree([3,9,20,15,7])
