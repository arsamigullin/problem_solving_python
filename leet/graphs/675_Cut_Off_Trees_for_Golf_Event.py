import collections
from heapq import heappop, heappush
from typing import List


class Solution:
    def cutOffTree(self, forest: List[List[int]]) -> int:
        if forest[0][0] == 0:
            return -1
        heap = []
        n = len(forest)
        m = len(forest[0])
        for i in range(n):
            for j in range(m):
                if i == 0 and j == 0:
                    continue
                if forest[i][j]>1:
                    heappush(heap, (forest[i][j], i,j))
        x,y = 0,0
        steps = 0
        while heap:
            dest_val, dest_x, dest_y = heappop(heap)
            #print(dest_val, forest[x][y])
            q = collections.deque([(forest[x][y], x, y, 0)])
            visited = set()
            while q:
                val, r, c, step = q.popleft()
                if (r,c) in visited:
                    continue
                if r == dest_x and c==dest_y:
                    x, y = dest_x, dest_y
                    steps+=step
                    break
                visited.add((r,c))
                for dx, dy in [[0,1],[0,-1],[1,0],[-1,0]]:
                    i = r + dx
                    j = c + dy
                    if 0<=i<n and 0<=j<m and (i,j) not in visited and forest[i][j] >= 1:
                        q.append((forest[i][j],i,j,step+1))
            else:
                return -1

        return steps

if __name__ == '__main__':
    s = Solution()
    s.cutOffTree([[54581641,64080174,24346381,69107959],[86374198,61363882,68783324,79706116],[668150,92178815,89819108,94701471],[83920491,22724204,46281641,47531096],[89078499,18904913,25462145,60813308]])