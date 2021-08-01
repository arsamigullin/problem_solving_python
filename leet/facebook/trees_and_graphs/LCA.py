# Definition for a binary tree node.
import  bisect
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def compose_tree(l, i):
    if i >= len(l) or l[i] is None:
        return None
    root = TreeNode(l[i])
    root.left = compose_tree(l, 2 * i + 1,)
    root.right = compose_tree(l, 2 * i + 2)
    return root


def find_node(root, val):
    if root is None:
        return None
    if root.val == val:
        return root
    l = find_node(root.left, val)
    if l is None:
        return find_node(root.right, val)
    else:
        return l


class Solution52ms:
    #Algo
    # 1. Calling cover to check if p is ancestor for q and conversely if q is ancestor for p
    # if one of them is an ancestor to the other return it
    # 2. Check if both p and q are in left branch
    # 3. if they both in left branch move further and search them in root.left
    # 4. if one is in left and another not return root since it is going to be lowest ancestor
    # 5. if they both not in left, proceed with the right branch
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if root is None or root is p or root is q:
            return root
        # 1
        if self.cover(p, q):
            return p
        # 1
        if self.cover(q, p):
            return q

        def helper(root, p, q):
            # 2
            p_left = self.cover(root.left, p)
            q_left = self.cover(root.left, q)

            # 4
            if p_left != q_left:
                return root
            # 3
            if p_left:
                return helper(root.left, p, q)
            #5
            else:
                return helper(root.right, p, q)

        return helper(root, p, q)

    def cover(self, root, node):
        if not root:
            return False

        if root is node:
            return True

        return self.cover(root.left, node) or self.cover(root.right, node)


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def find_path(node, v, path):

            if node is None:
                return ""
            p = str(node.val) if path == "" else path + '|' + str(node.val)
            if node.val == v:
                return p
            l_path = find_path(node.left, v, p)

            return l_path if l_path != "" else find_path(node.right, v, p)

        p_path = find_path(root, p.val, "").split('|')
        q_path = find_path(root, q.val, "").split('|')
        # print(q_path)
        # print(p_path)
        com = None
        for i in range(min(len(p_path), len(q_path))):
            if p_path[i] == q_path[i]:
                com = p_path[i]
            else:
                break
        return TreeNode(com)

# short and effective solution
# Algo
# Check if current node is p or q, if it is return it
# Check if left of current node is p or q, if it is return it
# Check if right of current node is p or q, if it is return it
# the lCA is going to be the current node at which both left and right are found
# if found only left or right return it
# if p and q are found return the current node
class SolutionShort(object):
    def lowestCommonAncestor(self, root, p, q):
        if not root: return None
        if p == root or q == root:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if left and right:
            return root
        if not left:
            return right
        if not right:
            return left

# solution from LeetCode

class Solution:

    def __init__(self):
        # Variable to store LCA node.
        self.ans = None
    # Algo
    # This is solved in post order manner
    # Iterate over current node left and see if p or q in left branch
    # Iterata over current node right and see if p or q in right branch
    # LCA is going to be the current node at which both  is_left_found and is_right_found true
    # OR either is_left_found or is_right_found is true and current node is p or q
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        def recurse_tree(current_node):

            # If reached the end of a branch, return False.
            if not current_node:
                return False

            # Left Recursion
            is_left_found = recurse_tree(current_node.left)

            # Right Recursion
            is_right_found = recurse_tree(current_node.right)

            # If the current node is one of p or q
            mid = current_node == p or current_node == q

            # it is not possible to have this sum greater than 2
            # because if current node is p or q hence only p or q can be found further
            # meaning the only is_left_found or is is_right_found can be true
            if mid + is_left_found + is_right_found >= 2:
                self.ans = current_node

            # Return True if either of the three bool values is True.
            return mid or is_left_found or is_right_found

        # Traverse the tree
        recurse_tree(root)
        return self.ans


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        lca = None

        def helper(node):
            if not node:
                return (False, False)
            nonlocal lca
            p_found_left, q_found_left = helper(node.left)
            p_found_right, q_found_right = helper(node.right)
            p_found = p_found_left or p_found_right or node == p
            q_found = q_found_left or q_found_right or node == q
            if p_found and q_found:
                lca = node
                return False, False
            return p_found, q_found

        helper(root)
        return lca

if __name__ == "__main__":
    root = compose_tree([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4], 0)
    sh = SolutionShort()
    sh.lowestCommonAncestor(root, find_node(root, 8), find_node(root, 0))
    s52 = Solution52ms()
    s52.lowestCommonAncestor(root, find_node(root, 8), find_node(root, 0))
