# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:

        stack = []
        stack_cl = []
        node = original
        node_cl = cloned
        while node or stack:
            if node is None:
                node = stack.pop()
                node_cl = stack_cl.pop()
                if node == target:
                    return node_cl
                node = node.right
                node_cl = node_cl.right
            else:
                stack.append(node)
                stack_cl.append(node_cl)
                node = node.left
                node_cl = node_cl.left