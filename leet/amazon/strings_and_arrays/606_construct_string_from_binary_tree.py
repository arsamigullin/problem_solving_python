#606. Construct String from Binary Tree

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def tree2str(self, t: TreeNode) -> str:
        if not t:
            return ""
        strtree = f"{t.val}"
        if t.left is None and t.right is None:
            return strtree
        elif t.right is None:
            strtree += f"({self.tree2str(t.left)})"
        elif t.left is None:
            strtree += f"()({self.tree2str(t.right)})"
        else:
            strtree += f"({self.tree2str(t.left)})({self.tree2str(t.right)})"
        return strtree
