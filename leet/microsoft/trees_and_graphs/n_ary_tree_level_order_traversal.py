
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

import collections
import typing
List = typing.List



class Solution:
    def levelOrderIterative(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []
        q = collections.deque([(root, 0)])
        res = []
        while q:
            node, level = q.popleft()
            if level + 1 == len(res):
                res[level].append(node.val)
            else:
                res.append([node.val])
            for child in node.children:
                if child:
                    q.append((child, level + 1))
        return res


    def levelOrderRecursive(self, root: 'Node') -> List[List[int]]:

        def traverse_node(node, level):
            if len(result) == level:
                result.append([])
            result[level].append(node.val)
            for child in node.children:
                traverse_node(child, level + 1)

        result = []

        if root is not None:
            traverse_node(root, 0)
        return result