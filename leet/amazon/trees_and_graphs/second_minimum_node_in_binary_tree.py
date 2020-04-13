
# this problem https://leetcode.com/problems/second-minimum-node-in-a-binary-tree/
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    '''
    Note: each node in the tree follows the rule
        root.val = min(root.left.val, root.right.val)

    Becasue of that the value at root is ALWAYS be smallest
    We visit the node ONLY if equals to the smallest, otherwise we compare it with the second smallest
    '''
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        m = root.val
        sec = float('inf')
        def helper(node):
            nonlocal sec
            if node:
                if m<node.val<sec:
                    sec = node.val
                elif node.val == m:
                    helper(node.left)
                    helper(node.right)

        helper(root)
        return -1 if sec == float('inf') else sec