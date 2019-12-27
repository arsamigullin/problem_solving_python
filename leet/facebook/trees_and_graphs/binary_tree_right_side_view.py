
# We using BFS here
# to know which level the current node at we store in the stack (node, height) pair
# we also maintain dictionary to store node at this particular height
# since this is stack we add left and THEN right nodes
# when popping it will bring right nodes first at particular level
class Solution:
    def rightSideView(self, root):
        stack = [(root, 1)]
        d = {}
        while len(stack) > 0:
            node, h = stack.pop()
            if node:
                if h not in d:
                    d[h] = node.val
                stack.append((node.left, h + 1))
                stack.append((node.right, h + 1))
        return d.values()