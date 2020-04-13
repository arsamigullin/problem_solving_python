import collections
from typing import List

import heapq
class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        n = len(heightMap)
        m = len(heightMap[0])
        if m <= 2 or n <= 2:
            return 0
        visited = [[False for j in range(m)] for i in range(n)]
        heap = []
        i, j ,dx, dy = 0, 0, 0, 1
        perimeter = n * 2 + (m - 2) * 2
		# collect boundary elements to the heap and mark them as visited
		# since water cannot stay on boundary elemets
        for _ in range(perimeter):
            heap.append((heightMap[i][j], i, j))
            visited[i][j] = True
            if dy + j == m:
                dx, dy = 1, 0
            elif dy + j == -1:
                dx, dy = -1, 0
            elif dx + i == n:
                dx, dy = 0, -1
            i+=dx
            j+=dy
        heapq.heapify(heap)
        total = 0
        while heap:
			# this will get next MIN value from where water can potentially leak
            MIN, k, l = heapq.heappop(heap)
			# we do BFS to find all the elements that are less than MIN value
            q = collections.deque([(k, l)])
            while q:
                i, j = q.popleft()
                for di, dj in [(0,1),(0,-1),(1,0),(-1,0)]:
                    x = i + di
                    y = j + dj
                    if 0<=x<n and 0<=y<m and not visited[x][y]:
                        visited[x][y] = True
                        if MIN > heightMap[x][y]:
                            total += MIN - heightMap[x][y]
                            q.append((x, y))
                        else:
							# we pusho onto heap every element that is greater or equal MIN
							# this value is going to be one of the next boundary value
                            heapq.heappush(heap, (heightMap[x][y], x,y))
        return total


class SolutionAttempt3:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        n = len(heightMap)
        m = len(heightMap[0])
        if m <= 2 or n <= 2:
            return 0
        _map = [[0]*m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                _map[i][j] = heightMap[i][j]
        total = 0
        for i in range(n - 2,0, -1):
            for j in range(m - 2, 0, -1):
                min_left = _map[i][j-1] if j == 1 else _map[i + 1][j]
                min_top = _map[i-1][j] if i == 1 else _map[i + 1][j]
                min_height = min(_map[i+1][j], _map[i][j+1], min_left, min_top)
                _map[i][j] = max(min_height, _map[i][j])


        for i in range(1,n-1):
            for j in range(1, m -1):
                min_height = min([_map[dx + i][dy + j] for dx, dy in [(0,1),(0,-1),(1,0),(-1,0)] if 0<=dx + i<n and 0<=dy + j<m ])
                _map[i][j] = min(min_height, heightMap[i][j])
                total+=max(0, min_height - heightMap[i][j])

        print(total)

class SolutionAttemp2:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        n = len(heightMap)
        m = len(heightMap[0])

        if m <= 2 or n <= 2:
            return 0
        heap = []
        _map = [[0]*m for _ in range(n)]#heightMap[:]
        for i in range(n):
            for j in range(m):
                _map[i][j] = heightMap[i][j]
        visited = set()
        total1 = 0
        total2 = 0
        def collect():
            _min = float('inf')
            heap.sort(key=lambda item: item[0], reverse=True)
            tot = 0
            while heap:
                h, v = heap.pop()
                _min = min(_min, h)
                tot += max(0, _min - v)
            return tot

        for i in range(1,n-1):
            for j in range(1, m -1):
                if (i-1, j) not in visited and (i, j-1) not in visited:
                    total1+=collect()
                min_right = _map[i][j+1] if j == m - 2 else _map[i - 1][j]
                min_down = _map[i+1][j] if i == n-2 else _map[i - 1][j]
                min_height = min(_map[i-1][j], _map[i][j-1], min_right, min_down)
                if min_height > _map[i][j]:
                    visited.add((i,j))
                    heap.append((min_height, _map[i][j]))
                elif min_height == _map[i][j]:
                    heap.append((min_height, _map[i][j]))
                    #heapq.heappush(heap, (min_height, map[i][j]))
                _map[i][j] = max(min_height, _map[i][j])
        total1+=collect()
        _map = [[0]*m for _ in range(n)]#heightMap[:]
        for i in range(n):
            for j in range(m):
                _map[i][j] = heightMap[i][j]
        for i in range(n-2,0,-1):
            for j in range(m-2, 0,-1):
                if (i+1, j) not in visited and (i, j+1) not in visited:
                    total2+=collect()
                min_right = _map[i][j-1] if j == m - 2 else _map[i + 1][j]
                min_down = _map[i-1][j] if i == n-2 else _map[i + 1][j]
                min_height = min(_map[i+1][j], _map[i][j+1], min_right, min_down)
                if min_height > _map[i][j]:
                    visited.add((i,j))
                    heap.append((min_height, _map[i][j]))
                elif min_height == _map[i][j]:
                    heap.append((min_height, _map[i][j]))
                    #heapq.heappush(heap, (min_height, map[i][j]))
                _map[i][j] = max(min_height, _map[i][j])

        total1 +=collect()
        return min(total1,total2)
class SolutionAttempt:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        n = len(heightMap)
        m = len(heightMap[0])
        if m <= 2 or n <= 2:
            return 0
        visited = set()
        def helper(q):
            MIN = float('inf')
            heap = []
            while q:
                i, j = q.popleft()
                visited.add((i, j))
                for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    x, y = i + dx, j + dy
                    if  0 <= x < n and 0 <= y < m  and  (x == 0 or x == n - 1 or y == 0 or y == m - 1):
                        MIN = min(MIN, heightMap[x][y])

                for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    x, y = i + dx, j + dy
                    if 1 <= x < n - 1 and 1 <= y < m - 1 and (x, y) not in visited:
                        if MIN > heightMap[x][y] and (x, y) not in visited:
                            visited.add((x, y))
                            q.append((x, y))

                if MIN > heightMap[i][j]:
                    heap.append(heightMap[i][j])

            return sum(MIN - x for x in heap if x < MIN)

        total = 0
        for i in range(1, n - 1):
            for j in range(1, m - 1):
                if (i, j) not in visited:
                    if any(heightMap[i][j] < heightMap[i + dx][j + dy] for dx, dy in
                           [(0, 1), (0, -1), (1, 0), (-1, 0)]):
                        total += helper(collections.deque([(i, j)]))
        return total

if __name__ == '__main__':
    s = Solution()

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

    s.trapRainWater(  [[2,2,2],
                        [2,1,2],
                        [2,1,2],
                        [2,1,2]])


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
    #s.trapRainWater([[9,9,9,9,9],[9,2,1,2,9],[9,2,8,2,9],[9,2,3,2,9],[9,9,9,9,9]])
    #s.trapRainWater([[5,8,7,7],[5,2,1,5],[7,1,7,1],[8,9,6,9],[9,8,9,9]])