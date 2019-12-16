# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        def find(node):
            if node is None:
                return 0
            res = min(find(node.left), find(node.right)) + 1
            return res

        return find(root);

if __name__ == "__main__":
    t1 = TreeNode(2)
    t2 = TreeNode(1)
    t1.left = t2

    s = Solution()
    print(s.minDepth(t1))
