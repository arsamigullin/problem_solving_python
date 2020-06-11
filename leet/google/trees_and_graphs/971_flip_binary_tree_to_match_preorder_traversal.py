from typing import List

# preorder traversal

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    '''
    if node is not equal of jth voyage item
    that means it is not possible
    so, root of subtree must be equal of jth voyage item

    if the left ite is not equal to the jth voyage item that means
    we can try to swap left and right child by calling helper with right node passed first
    (kind if imitation of swapping)

    if left is equal to the current ith voyage item
    we do regular dfs with left child first

    '''
    def flipMatchVoyage(self, root: TreeNode, voyage: List[int]) -> List[int]:
        j = 0
        res = []
        def helper(node):
            nonlocal j, res
            if node:
                if node.val!=voyage[j]:
                    res = [-1]
                    return
                j+=1
                if node.left and node.left.val != voyage[j]:
                    res.append(node.val)
                    helper(node.right)
                    helper(node.left)
                else:
                    helper(node.left)
                    helper(node.right)
        helper(root)
        if res and res[0] == -1:
            return [-1]
        return res