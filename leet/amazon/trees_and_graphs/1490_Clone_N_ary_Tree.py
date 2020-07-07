
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []


class Solution:
    def cloneTree(self, root: 'Node') -> 'Node':

        def dfs(node):
            if not node:
                return None
            parent = Node(node.val, [])
            for child in node.children:
                copychld = dfs(child)
                if copychld:
                    parent.children.append(copychld)
            return parent

        return dfs(root)