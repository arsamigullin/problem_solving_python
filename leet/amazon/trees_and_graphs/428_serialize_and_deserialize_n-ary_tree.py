"""
# Definition for a Node.

"""
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Codec:
    '''
    the key idea is preorder traversal and and keeping children length next to the val of node
    '''

    def serialize(self, root: 'Node') -> str:
        if not root:
            return None
        preorder = []
        def dfs(node):
            if not node:
                return
            preorder.append(str(node.val) + ":" + str(len(node.children)))
            for child in node.children:
                dfs(child)

        dfs(root)
        return '|'.join(preorder)

    def deserialize(self, data: str) -> 'Node':
        if not data:
            return None
        data = data.split('|')
        i = 0
        def dfs():
            nonlocal i
            val, childCnt = data[i].split(':')
            root = Node(int(val), [])
            if childCnt == "0":
                return root
            for ch in range(int(childCnt)):
                i += 1
                root.children.append(dfs())
            return root

        return dfs()
