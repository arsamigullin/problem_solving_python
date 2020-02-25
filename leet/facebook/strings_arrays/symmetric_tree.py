# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

import collections
# Observation
# if we had devised the tree on two halves we would notice
# the nodes on the left can be appended to the stack and the nodes right can be popped from stack
# so, if tree is symmetric the stack at each level would be empty
# Algo
# 1.we assign negative level to all the nodes of left subtree 
# 2.we assign positive level to all the nodes of right subtree
# 3.Then if level node is negative we append that node to the stack in dict at abs(level)
# 4. if level node is positive we compare the popped value and current value of node
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        sentinel = float('inf')
        d = collections.defaultdict(list)
        q = collections.deque([(root,0)])
        while q:
            node, level = q.popleft()
            nodeval = sentinel if node is None else node.val
            if level < 0:
                d[abs(level)].append(nodeval)
            elif level > 0:
                if not d[level] or d[level].pop() != (nodeval):
                    return False
            if node:
                # here we assign levels based on the current level
                a, b = -1, 1 # this will used when the current level is 0
                if level != 0:
                    a = b = level//abs(level)
                q.append((node.left, level + a))
                q.append((node.right, level + b))
        return True

# very interesting solution 
# we do isMirror for the same node level but from different subtrees
class SolutionRecursive:
    def isSymmetric(self, root: TreeNode) -> bool:
        def isMirror(t1, t2):
            if t1 is None and t2 is None:
                return True
            if t1 is None or t2 is None:
                return False
            return (t1.val == t2.val) and isMirror(t1.right, t2.left) and isMirror(t1.left, t2.right)
        
        return isMirror(root, root)

if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(2)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(4)

    root.right.left = TreeNode(4)
    root.right.right = TreeNode(3)
    s = SolutionRecursive()
    s.isSymmetric(root)

