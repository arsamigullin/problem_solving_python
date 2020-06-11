# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:

        cnt = 0

        def helper(node):
            nonlocal cnt
            if not node:
                return 0, False
            left, isFound = helper(node.left)
            if isFound:
                return left, isFound
            cnt += 1
            if k == cnt:
                return node.val, True
            right, isFound = helper(node.right)
            if isFound:
                return right, isFound
            return 0, False

        return helper(root)[0]


class Solution:
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        stack = []

        while True:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            k -= 1
            if not k:
                return root.val
            root = root.right # the next iteration will collect all the left children of the root.right node

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:

        stack = []
        node = root
        while stack or node:
            if node is None:
                node = stack.pop()
                k-=1
                if k == 0:
                    return node.val
                node = node.right
            else:
                stack.append(node)
                node = node.left


class Solution:
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """

        def inorder(r):
            return inorder(r.left) + [r.val] + inorder(r.right) if r else []

        return inorder(root)[k - 1]