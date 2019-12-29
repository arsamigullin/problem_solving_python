# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
# https://leetcode.com/problems/smallest-subtree-with-all-the-deepest-nodes/
# 1. Important to understand what you are asked about
# 2. We need to return a subtree with the deepest node among another nodes
# consider three different examples this tree
#     0           0            0
#   /  \         / \          / \
#  3    5       3   5        3   5
# /            /    \       / \
# 4           4      2     4   7
# 3.for the first tree the answer is node 4
# 4.for the second tree the answer is node 0
# 5.for the second tree the answer is 3
# if at the particular root the depth of left and right parts equal return this root node with left depth
# if left depth > right depth return left node with left depth
# if rigth depth > left depth return right node with right depth
#
# in the second example at root 3 and 5 we will return (4,2) and (2,2) accordingly
# then at node 0 we will see that their depth is equal and we will return node 0
class Solution:

    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        def find(root):
            if root is None:
                return (None, 0)
            L, ldist = find(root.left)
            R, rdist = find(root.right)
            if ldist > rdist:
                return (L, ldist + 1)
            if ldist < rdist:
                return (R, rdist + 1)

            return (root, ldist + 1)
        return find(root)[0]





# this is actually the same, but here we find the depth first and then we processing
# the tree
class Solution(object):
    def subtreeWithAllDeepest(self, root):
        # Tag each node with it's depth.
        depth = {None: -1}
        def dfs(node, parent = None):
            if node:
                print(f"{node.val} d {depth[parent] + 1}")
                depth[node] = depth[parent] + 1
                dfs(node.left, node)
                dfs(node.right, node)
        dfs(root)

        max_depth = max(depth.values())

        def answer(node):
            # Return the answer for the subtree at node.
            d = depth.get(node, None)
            if not node or d == max_depth:
                return node
            L, R = answer(node.left), answer(node.right)
            print(f"{'None' if L is None else L.val} {'None' if R is None else R.val} {node.val}")
            return node if L and R else L or R

        return answer(root)

def compose_tree(l, i):
    if i>=len(l) or l[i] is None:
        return None
    t = TreeNode(l[i])
    t.left = compose_tree(l, 2*i+1)
    t.right = compose_tree(l, 2 * i + 2)
    return t


root = compose_tree([0,3,1,4,8,2,None,None,6,None,None,None,5], 0)

if __name__ == "__main__":
    s = Solution()
    n=s.subtreeWithAllDeepest(root)
    print(n.val)