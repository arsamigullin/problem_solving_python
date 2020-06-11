# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def flipEquiv(self, root1: TreeNode, root2: TreeNode) -> bool:
        if (not root1 and root2) or (root1 and not root2):
            return False
        elif not root1 and not root2:
            return True
        elif root1.val == root2.val:
            if (not root1.left and not root2.left) or (not root1.right and not root2.right):
                return self.flipEquiv(root1.left, root2.left) and self.flipEquiv(root1.right, root2.right)
            elif root1.left and root2.left and root1.right and root2.right and root1.left.val == root2.left.val and root1.right.val == root2.right.val:
                return self.flipEquiv(root1.left, root2.left) and self.flipEquiv(root1.right, root2.right)
            else:
                return self.flipEquiv(root1.left, root2.right) and self.flipEquiv(root1.right, root2.left)
        return False


class Solution:
    def flipEquiv(self, root1, root2):
        def dfs(node):
            if node:
                yield node.val
                L = node.left.val if node.left else -1
                R = node.right.val if node.right else -1
                if L < R:
                    yield from dfs(node.left)
                    yield from dfs(node.right)
                else:
                    yield from dfs(node.right)
                    yield from dfs(node.left)
                yield '#'

        return all(x == y for x, y in itertools.zip_longest(
            dfs(root1), dfs(root2)))


if __name__ == '__main__':
    s = Solution()
    t1 = TreeNode(2)
    t2 = TreeNode(2)
    print(t1 is t2)