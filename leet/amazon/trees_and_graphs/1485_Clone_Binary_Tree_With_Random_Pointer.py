# Definition for Node.
# class Node:
#     def __init__(self, val=0, left=None, right=None, random=None):
#         self.val = val
#         self.left = left
#         self.right = right
#         self.random = random


class NodeCopy:
    def __init__(self, val=0, left=None, right=None, random=None):
        self.val = val
        self.left = left
        self.right = right
        self.random = random

# two pass solution
class Solution:
    def copyRandomBinaryTree(self, root: 'Node') -> 'NodeCopy':
        d = {}

        def copyLeftRight(node):
            if not node:
                return None
            nd = NodeCopy(node.val, copyLeftRight(node.left), copyLeftRight(node.right))
            d[node] = nd
            return nd

        copyNode = copyLeftRight(root)

        def copyRandom(node, copyNode):
            if not node:
                return
            copyNode.random = d.get(node.random, None)
            copyRandom(node.left, copyNode.left)
            copyRandom(node.right, copyNode.right)

        copyRandom(root, copyNode)

        return copyNode


# one pass solution


# Definition for Node.
# class Node:
#     def __init__(self, val=0, left=None, right=None, random=None):
#         self.val = val
#         self.left = left
#         self.right = right
#         self.random = random

class Solution:
    def copyRandomBinaryTree(self, root: 'Node') -> 'NodeCopy':
        visited = {}
        return self.dfs(root, visited)

    def dfs(self, node, visited):
        if node is None:
            return None

        if node in visited:
            return visited[node]

        copyNode = NodeCopy(node)
        visited[node] = copyNode

        copyNode.left = self.dfs(node.left, visited)
        copyNode.right = self.dfs(node.right, visited)
        copyNode.random = self.dfs(node.random, visited)
        copyNode.val = node.val

        return copyNode

