# Definition for a binary tree node.
import collections
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        d = collections.defaultdict(dict)
        q = collections.deque([[root, 0, 0]])
        while q:
            node, lvl, depth = q.popleft()
            d[lvl].setdefault(depth, []).append(node.val)
            if node.left:
                q.append([node.left, lvl - 1, depth + 1])
            if node.right:
                q.append([node.right, lvl + 1, depth + 1])

        res = []
        for k in sorted(d.keys()):
            data = []
            for ki in sorted(d[k]):
                data += sorted(d[k][ki])
            res.append(data)
        return res


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        node_list = []

        def BFS(root):
            queue = deque([(root, 0, 0)])
            while queue:
                node, row, column = queue.popleft()
                if node is not None:
                    node_list.append((column, row, node.val))
                    queue.append((node.left, row + 1, column - 1))
                    queue.append((node.right, row + 1, column + 1))

        # step 1). construct the global node list, with the coordinates
        BFS(root)

        # step 2). sort the global node list, according to the coordinates
        # note: this will have proper order
        node_list.sort()

        # step 3). retrieve the sorted results partitioned by the column index
        ret = OrderedDict()
        for column, row, value in node_list:
            if column in ret:
                ret[column].append(value)
            else:
                ret[column] = [value]

        return ret.values()