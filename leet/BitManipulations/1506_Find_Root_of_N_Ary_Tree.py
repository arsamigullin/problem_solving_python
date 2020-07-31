# Definition for a Node.
import collections
from typing import List


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []
        self.visited = False

class Solution1:
    def findRoot(self, tree: List['Node']) -> 'Node':
        ans = 0
        for node in tree:
            ans ^= node.val
            for child in node.children:
                ans ^= child.val
        for node in tree:
            if ans == node.val:
                return node


class Solution:
    def findRoot(self, tree: List['Node']) -> 'Node':
        if not tree:
            return None
        if len(tree) == 1:
            return tree[0]
        d = collections.defaultdict(int)

        # this is recursive solution
        # and it is much much longer than iterative and results in TLE
        #

        # def dfs(node):
        #     if not node:
        #         return
        #     for child in node.children:
        #         if child.val not in d:
        #             d[child] += 1
        #             dfs(child)
        #
        # for t in tree:
        #     if t in d:
        #         d[t] += 1
        #     else:
        #         d[t] = 0
        #         dfs(t)
        # print(d)

        # this is iterative solution
        # it is fast
        for t in tree:
            if t in d:
                d[t] +=1
            else:
                d[t] = 0

            for child in t.children:
                d[child]+=1

        return [key for key in d if d[key] == 0][0]


