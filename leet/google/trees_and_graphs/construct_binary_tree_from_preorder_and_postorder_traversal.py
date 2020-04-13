# Definition for a binary tree node.
# this problem
# 889. Construct Binary Tree from Preorder and Postorder Traversal

# similar
# 106. Construct Binary Tree from Inorder and Postorder Traversal
# 105. Construct Binary Tree from Preorder and Inorder Traversal
from typing import List


class Solution:
    '''
    This is genius

    we maintain two global variable (i and j)
    i is incrementing whenever we entered the function and created the node
    j is incrementing right before exiting the function

    i is to pick up the value for node from pre array
    j is to limit recursion

    pre = [1,2,4,5,3,6,7]
    post= [4,5,2,6,7,3,1]

    initially i and j are 0

    we do dfs until node.val of current node is not equal to the post[j]
    '''
    i = j = 0
    def constructFromPrePost(self, pre: List[int], post: List[int]) -> TreeNode:
        p = TreeNode(pre[self.i])
        self.i += 1
        if p.val != post[self.j]:
            p.left = self.constructFromPrePost(pre, post)
        if p.val != post[self.j]:
            p.right = self.constructFromPrePost(pre, post)
        self.j += 1
        return p


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class SolutionAttempt:
    def constructFromPrePost(self, pre: List[int], post: List[int]) -> TreeNode:
        dpre = {val: i for i, val in enumerate(pre)}
        dpos = {val: i for i, val in enumerate(post)}
        def helper(start, end, val):
            if start>=end:
                return None

            root = TreeNode(val)
            root.left  = helper(start + 1, end - 1, pre[start+1])
            root.right = helper(start + 1, end - 1, post[end-1])
            return root
        node = helper(0, len(pre)-1, pre[0])
        print('done')


if __name__ == '__main__':
    s = Solution()
    s.constructFromPrePost([1,2,4,5,3,6,7], [4,5,2,6,7,3,1])