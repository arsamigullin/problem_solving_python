"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []
"""
import heapq

# fast
class Solution:
    def diameter(self, root: 'Node') -> int:
        """
        :type root: 'Node'
        :rtype: int
        """

        self.max_distance = 0

        def dfs(root):
            if root.children == []:
                return 1

            max1, max2 = 0, 0

            for child in root.children:
                d = dfs(child)
                if d > max2:
                    max2 = d
                    if max2 > max1:
                        max1, max2 = max2, max1

            self.max_distance = max(self.max_distance, max1 + max2)
            return max1 + 1

        dfs(root)
        return self.max_distance


class SolutionMy:
    def diameter(self, root: 'Node') -> int:
        """
        :type root: 'Node'
        :rtype: int
        """
        res = float('-inf')

        def dfs(node):
            nonlocal res
            if not node:
                return 0
            heap = []
            cld = []
            for child in node.children:
                cld.append(child.val)
                heapq.heappush(heap, -dfs(child))
            m1 = 0
            m2 = 0
            if len(heap) >= 2:
                m1 = abs(heapq.heappop(heap))
                m2 = abs(heapq.heappop(heap))
                res = max(res, m1 + m2)
            elif len(heap) == 1:
                m1 = abs(heapq.heappop(heap))
                res = max(res, m1)

            return max(m1, m2) + 1

        return max(dfs(root) - 1, res)


