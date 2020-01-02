import collections
# https://leetcode.com/problems/shortest-distance-from-all-buildings/
# Algo:
# 1. Build graph in adjacency list
# the parent is current cell grid[i][j], the children are neighbors cells
# so each node will have no more that 4 children
# 2. While building the graph also gather all ones
# 3.for each 1 we going to calculate the shortest path from all the nodes to that 1 using BFS
# 4.Initially we initialize the queue with neighbor nodes of that particular 1
# 5.See if the node has been visited, if so skip it
class Solution:
    def shortestDistance(self, grid: list) -> int:
        adj_list = {}
        ones = []
        # 1 and 2
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                l = []
                if grid[i][j] == 0:
                    if i-1 >= 0 and grid[i - 1][j] == 0:
                        l.append((i - 1, j))
                    if j - 1 >= 0 and grid[i][j - 1] == 0:
                        l.append((i, j - 1))
                    if i + 1 < len(grid) and grid[i + 1][j] == 0:
                        l.append((i + 1, j))
                    if j + 1 < len(grid[0]) and grid[i][j + 1] == 0:
                        l.append((i, j + 1))
                    adj_list[(i, j)] = l
                elif grid[i][j] == 1:
                    ones.append((i,j))
        paths = collections.defaultdict(list)
        # 3
        for t in range(len(ones)):
            visited = {}
            target = ones[t]
            x, y = target
            queue = collections.deque()
            #4
            if (x-1, y) in adj_list:
                queue.append((x-1, y, 1))
            if (x+1, y) in adj_list:
                queue.append((x + 1, y, 1))
            if (x, y -1) in adj_list:
                queue.append((x, y -1, 1))
            if (x, y + 1) in adj_list:
                queue.append((x, y + 1, 1))

            while len(queue) > 0:
                i, j, d = queue.popleft()
                if (i,j) in visited:
                    continue
                else:
                    visited[(i,j)] = 1
                    if len(paths[(i,j)]) == 0:
                        paths[(i, j)] = [0, 0]
                    paths[(i,j)][0] += d # store distance
                    paths[(i, j)][1] += 1 # store length

                children = adj_list[(i,j)]
                for child in children:
                    n, m = child
                    if child in visited:
                        continue
                    queue.append((n, m, d + 1))
        m = float('inf')
        for v in paths.values():
            # we should consider only the node that reached all the ones
            if v[1] == len(ones):
                m = min(m, v[0])
        return -1 if m == float('inf') else m

if __name__ == "__main__":
    s = Solution()
    s.shortestDistance([[1,1,1,1,1,1,1,0],
 [0,0,0,0,0,0,0,1],
 [1,1,1,1,1,1,0,1],
 [1,0,0,0,0,1,0,1],
 [1,0,1,1,0,1,0,1],
 [1,0,1,0,0,1,0,1],
 [1,0,1,1,1,1,0,1],
 [1,0,0,0,0,0,0,1],
 [0,1,1,1,1,1,1,0]])
    s.shortestDistance([[1,1,1,1,1,0],
                        [0,0,0,0,0,1],
                        [0,1,1,0,0,1],
                        [1,0,0,1,0,1],
                        [1,0,1,0,0,1],
                        [1,0,0,0,0,1],
                        [0,1,1,1,1,0]])
    s.shortestDistance([[1,0,1,0,1]])
    s.shortestDistance([[1,0],[0,1]])
    s.shortestDistance([[1,0,2,0,1],[0,0,0,0,0],[0,0,1,0,0]])
