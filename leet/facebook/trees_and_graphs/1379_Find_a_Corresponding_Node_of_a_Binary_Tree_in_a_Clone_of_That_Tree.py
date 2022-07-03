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
        while stack or node:
            # as long as node is not None we try to go deeper
            if node:
                if node == target:
                    return node_cl
                # we also collect nodes to visit right nodes once we've reached the bottom of the left branch
                stack.append(node)
                stack_cl.append(node_cl)
                node = node.left
                node_cl = node_cl.left
            else:
                node = stack.pop()
                node_cl = stack_cl.pop()
                node = node.right
                node_cl = node_cl.right
        return None