# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
# many tree problems are solved using additional memory
# we have here too self.l = []
# we will collect here all the nodes in InOrder traversal
# then will iterate over self.l and assign the nodes from it to root
class Solution:
    def __init__ (self):
        self.l = []

    def flatten(self, root: TreeNode) -> None:
        def find(node):
            if node is None:
                return
            self.l.append(node)
            find(node.left)
            find(node.right)
        find(root)
        node = root #not to lose link to root

        # start from 1, because in self.l[0] root is stored
        for i in range(1, len(self.l)):
            node.left = None
            node.right = self.l[i]
            node = node.right








if __name__ == "__main__":

    t = [1,2,5,3,4,None,6]
    root = TreeNode(0)
    def create(node, i):
        if i >= len(t) or node is None:
            return
        node.val = t[i]
        if 2*i + 1 < len(t) and t[2*i+1] is not None:
            node.left = TreeNode(0)
        if 2*i + 2 < len(t) and t[2*i+2] is not None:
            node.right = TreeNode(0)
        create(node.left, 2 * i + 1)
        create(node.right, 2 * i + 2)
    create(root, 0)

    def f():
        return (1,2)
    a,b = f()
    s = Solution()
    s.flatten(root)
    print('done')