"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

# similar problem
# 160. Intersection of Two Linked Lists

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        orig_p = p
        orig_q = q
        while p!=q:
            p = p.parent
            q = q.parent
            if not p:
                p = orig_q
            if not q:
                q = orig_p
        return q