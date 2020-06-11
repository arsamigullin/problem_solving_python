class Solution:
    def __init__(self):
        self.total = 0

    # here we start to increment count of edges from the bottom
    def diameterOfBinaryTree(self, root) -> int:
        def find(node):
            if node is None:
                return -1 # since we count edges not nodes we need to decrease cnt
            l_max = find(node.left) + 1
            r_max = find(node.right) + 1
            self.total = max(self.total, l_max + r_max)
            return max(l_max, r_max)

        return max(find(root), self.total)



