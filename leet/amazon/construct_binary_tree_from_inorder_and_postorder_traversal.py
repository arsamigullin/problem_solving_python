# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# Observations
# Inorder traversal splits the the array on two halves
# for example
# inorder [4, 2, 5, 1, 6, 3, 7],
# postorder [4, 5, 2, 6, 7, 3, 1]. The root is 1
# 1 splits inorder on two halves
# before start we mapping inorder to the dict where key is val and value is index
# On each iteration we popping from postorder and create a root
# IMPORTANT
# since in the postorder the right nodes comes close to the root (1)
# we start form the node from its RIGHT child

class Solution:
    def buildTree(self, inorder: list, postorder: list) -> TreeNode:
        def helper(in_left, in_right):
            # if there is no elements to construct subtrees
            if in_left > in_right:
                return None

            # pick up the last element as a root
            val = postorder.pop()
            root = TreeNode(val)

            # root splits inorder list
            # into left and right subtrees
            index = idx_map[val]

            # build right subtree
            # Important! we constantly popping from postorder since the roots are stored on the righ side
            root.right = helper(index + 1, in_right)
            # build left subtree
            root.left = helper(in_left, index - 1)
            return root

        # build a hashmap value -> its index
        idx_map = {val: idx for idx, val in enumerate(inorder)}
        return helper(0, len(inorder) - 1)

if __name__ == "__main__":
    s = Solution()
    s.buildTree([4, 2, 5, 1, 6, 3, 7], [4, 5, 2, 6, 7, 3, 1])

