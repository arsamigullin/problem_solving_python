# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# recursive
class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        num = 0
        if not root:
            return 0

        def helper(node, val):
            nonlocal num
            val = val * 10 + node.val
            if not node.left and not node.right:
                num+=val
                return
            if node.left:
                helper(node.left, val)
            if node.right:
                helper(node.right, val)

        helper(root, 0)
        return num

# iterative
class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        if not root:
            return 0

        stack = [(root, 0)]
        val = 0

        while stack:
            node, curnum = stack.pop()
            if node is not None:
                curnum = curnum * 10+ node.val
                if node.left is None and node.right is None:
                    val += curnum
                else:
                    stack.append((node.left, curnum))
                    stack.append((node.right, curnum))
        return val


if __name__ == '__main__':
    node = TreeNode(4)
    node.right = TreeNode(0)
    node.left = TreeNode(9)
    node.left.right = TreeNode(1)
    node.left.left = TreeNode(5)
    s = SolutionIter()
    s.sumNumbers(node)
