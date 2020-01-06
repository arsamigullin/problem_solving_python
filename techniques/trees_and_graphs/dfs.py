class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right =  right


l = [1, 2, 3, 5, 7, 9, 6, None, 8, 9, None]
root = TreeNode()

def compose_tree(l, i):
    if i >= len(l) or l[i] is None:
        return None
    return TreeNode(l[i], compose_tree(l, 2*i+1), compose_tree(l, 2*i+2))

from collections import  deque
queue = deque()

#dfs
def trav (root):
    if root is None:
        return
    #nonlocal queue
    queue.append(root)
    trav(root.left)
    trav(root.right)



if __name__ == "__main__":

    node = compose_tree(l, 0)
    trav(node)
    print(deque)
    print('done')

"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""


class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        if root is None:
            return root
        first, last = None, None

        def convertToDll(node):
            nonlocal first, last
            if node:

                convertToDll(node.left)
                if last:
                    last.right = node
                    node.left = last
                else:
                    first = node
                last = node
                convertToDll(node.right)

        convertToDll(root)
        last.rigth = first
        first.left = last
        return first
