import collections
from typing import List
import heapq


class SolutionMyCorrectFast:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        n = len(heightMap)
        m = len(heightMap[0])
        if m <= 2 or n <= 2:
            return 0
        visited = [[False for _ in range(m)] for _ in range(n)]
        heap = []
        i, j, dx, dy = 0, 0, 0, 1
        perimeter = n * 2 + (m - 2) * 2
        for _ in range(perimeter):
            heap.append((heightMap[i][j], i, j))
            visited[i][j] = True
            if dy + j == m:
                dx, dy = 1, 0
            elif dy + j == -1:
                dx, dy = -1, 0
            elif dx + i == n:
                dx, dy = 0, -1
            i += dx
            j += dy
        heapq.heapify(heap)
        total = 0
        while heap:
            MIN, k, l = heapq.heappop(heap)
            q = collections.deque([(k, l)])
            while q:
                i, j = q.popleft()
                for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    x = i + di
                    y = j + dj
                    if 0 <= x < n and 0 <= y < m and not visited[x][y]:
                        visited[x][y] = True
                        if MIN > heightMap[x][y]:
                            total += MIN - heightMap[x][y]
                            q.append((x, y))
                        else:
                            heapq.heappush(heap, (heightMap[x][y], x, y))
        return total


class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        n = len(heightMap)
        m = len(heightMap[0])
        if m <= 2 or n <= 2:
            return 0

        #visited = set()
        visited = [[False for j in range(m)] for i in range(n)]
        heap = []
        i, j ,dx, dy = 0, 0, 0, 1
        perimeter = n * 2 + (m - 2) * 2
        for _ in range(perimeter):
            heapq.heappush(heap, (heightMap[i][j], i, j))
            visited[i][j] = True
            if dy + j == m:
                dx, dy = 1, 0
            elif dy + j == -1:
                dx, dy = -1, 0
            elif dx + i == n:
                dx, dy = 0, -1
            i+=dx
            j+=dy
        total = 0
        while heap:
            MIN, k, l = heapq.heappop(heap)
            #if (x,y) in visited:
                #continue
            q = collections.deque([(k, l)])
            while q:
                i, j = q.popleft()
                #visited[i][j] = True
                for dx, dy in [(0,1),(0,-1),(1,0),(-1,0)]:
                    x = i + dx
                    y = j + dy
                    if 0<=x<n and 0<=y<m and not visited[x][y]:
                        if MIN > heightMap[x][y]:
                            #if 1<=x<n-1 and 1<=y<m-1:
                            total += MIN - heightMap[x][y]
                            visited[x][y] = True
                            q.append((x, y))
                        else:
                            heapq.heappush(heap, (heightMap[x][y], x,y))
        return total

class SolutionCorrect:
    def trapRainWater(self, heightMap):
        """
        """
        m = len(heightMap)
        if m <= 2:
            return 0
        n = len(heightMap[0])
        if n <= 2:
            return 0
        visited = [[False for j in range(n)] for i in range(m)]
        pq = []
        candidates = ([(i, 0) for i in range(m)] +
                      [(i, n-1) for i in range(m)] +
                      [(0, j) for j in range(1, n-1)] +
                      [(m-1, j) for j in range(1, n-1)])
        for i, j in candidates:
            visited[i][j] = True
            pq.append((heightMap[i][j], i, j))
        heapq.heapify(pq)
        trapped = 0
        while pq:
            h, i, j = heapq.heappop(pq)
            dfsStack = collections.deque([(i, j)])
            while dfsStack:
                i, j = dfsStack.popleft()
                neighbors = [(i-1,j), (i+1,j), (i,j-1), (i,j+1)]
                for k, l in neighbors:
                    if k<0 or l<0 or k>=m or l>=n or visited[k][l]:
                        continue
                    visited[k][l] = True
                    if heightMap[k][l] < h:
                        toAdd = h - heightMap[k][l]
                        trapped += toAdd
                        dfsStack.append((k, l))
                    else:
                        heapq.heappush(pq, (heightMap[k][l], k, l))
        return trapped

class MySolution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        n = len(heightMap)
        m = len(heightMap[0])
        if m <= 2 or n <= 2:
            return 0

        visited = set()
        heap = []
        i, j ,dx, dy = 0, 0, 0, 1
        perimeter = n * 2 + (m - 2) * 2
        for _ in range(perimeter):
            heapq.heappush(heap, (heightMap[i][j], (i, j)))
            i+=dx
            j+=dy
            if j == m:
                dx, dy = 1, 0
                j-=1
            elif j == 0:
                dx, dy = -1, 0
            elif i == n:
                dx, dy = 0, -1
                i-=1
        total = 0
        while heap:
            MIN, (x, y) = heapq.heappop(heap)
            if (x,y) in visited:
                continue
            q = collections.deque([(x, y)])
            while q:
                i, j = q.popleft()
                visited.add((i,j))
                for dx, dy in [(0,1),(0,-1),(1,0),(-1,0)]:
                    x = i + dx
                    y = j + dy
                    if 0<=x<n and 0<=y<m and (x,y) not in visited:
                        if MIN > heightMap[x][y]:
                            if 1<=x<n-1 and 1<=y<m-1:
                                total += MIN - heightMap[x][y]
                                visited.add((x, y))
                                q.append((x, y))
                        else:
                            heapq.heappush(heap, (heightMap[x][y], (x,y)))
        return total

if __name__ == '__main__':
    s = Solution()
    s.trapRainWater(
[[12,13,1,12],[13,4,13,12],[13,8,10,12],[12,13,12,12],[13,13,13,13]])
    s.trapRainWater(  [[2,2,2],
                        [2,1,2],
                        [2,1,2],
                        [2,1,2]])

    s.trapRainWater([[13, 16, 15, 18, 15, 15],
                     [14, 1, 8, 9, 7, 9],
                     [19, 5, 4, 2, 5, 10],
                     [13, 1, 7, 9, 10, 3],
                     [17, 7, 5, 10, 6, 1],
                     [15, 9, 8, 2, 8, 3]])

    s.trapRainWater([[5, 8, 7, 7],
                     [5, 2, 1, 5],
                     [7, 1, 7, 1],
                     [8, 9, 6, 9],
                     [9, 8, 9, 9]])




    s.trapRainWater([[9,9,9,9,9,9,8,9,9,9,9],
 [9,0,0,0,0,0,1,0,0,0,9],
 [9,0,0,0,0,0,0,0,0,0,9],
 [9,0,0,0,0,0,0,0,0,0,9],
 [9,9,9,9,9,9,9,9,9,9,9]])
    s.trapRainWater(   [[78,16,94,36],
    [87,93,50,22],
    [63,28,91,60],
    [64,27,41,27],
    [73,37,12,69],
    [68,30,83,31],
    [63,24,68,36]])
    s.trapRainWater( [[12,13,1,12],
  [13,4,13,12],
  [13,8,10,12],
  [12,13,12,12],
  [13,13,13,13]])
    s.trapRainWater([[5,8,7,7],
 [5,2,1,5],
 [7,1,7,1],
 [8,9,6,9],
 [9,8,9,9]])