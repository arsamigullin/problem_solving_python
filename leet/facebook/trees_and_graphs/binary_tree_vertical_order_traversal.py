import collections

from trees_and_graphs.dfs import TreeNode
#https://leetcode.com/problems/binary-tree-vertical-order-traversal/
# Algo
# 1. Usign BFS we assign idx starting from root. Root will always have 0
# 2. We increase idx when adding left node and decreasing when adding right node
# 3. Visited node we add to the visited array
# 4. we also keep tracking max_idx and min_idx to determine result array boundary
# 5. After BFS we define res array with length (max_idx-min_idx+1)
# we fill this array from visited array where ieach item contains idx
# to compute index for res array we subtract max_idx - idx

class Solution:
    def verticalOrder(self, root: TreeNode) -> list:
        if root is None:
            return []
        queue = collections.deque([(root, 0)])
        visited = []
        max_idx = 0
        min_idx = 0
        while len(queue) > 0:
            node, idx = queue.popleft()
            max_idx = max(max_idx, idx)
            min_idx = min(min_idx, idx)
            visited.append((node, idx))
            if node.left:
                queue.append((node.left, idx+1))
            if node.right:
                queue.append((node.right, idx-1))
        res = [[] for _ in range(max_idx-min_idx+1)]
        print(max_idx)
        print(min_idx)
        for i in range(len(visited)):
            node, idx = visited[i]
            res[max_idx - idx].append(node.val)
        return res