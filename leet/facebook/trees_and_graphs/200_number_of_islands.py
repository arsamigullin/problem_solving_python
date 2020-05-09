
# this is dfs approach
# once we encountered '1' we can increase total and reset 1 to 0 for that cell.
# then we will go through all neighbors which have 1 until all the neighbors are 0
# since we marked reset 1 to the next 1 we encounter will increase total
class Solution1:
    def numIslands(self, grid) -> int:
        total = 0

        def dfs(i, j):
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == '0':
                return
            grid[i][j] = '0'
            dfs(i - 1, j)
            dfs(i + 1, j)
            dfs(i, j - 1)
            dfs(i, j + 1)

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == '1':
                    total += 1
                    dfs(i, j)

        return total

# this is bfs
# onde we encountered '1' we continue to go through its neighbours using queue.
# We adding item to queue if this item is equal '1'.
# queue contains key that is formed by formula i*len(grid[0])+j
# If queue is empty
# there is no neighbors anymore.
import collections
class Solution:
    def numIslands(self, grid) -> int:
        queue = collections.deque()
        total = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == '0':
                    continue
                total+=1
                grid[i][j] = '0'
                queue.append(i*len(grid[0]) + j)
                while len(queue) > 0:
                    id = queue.popleft()
                    k = id//len(grid[0])
                    r = id % len(grid[0])
                    if k - 1 >=0 and grid[k - 1][r] == '1':
                        grid[k - 1][r] = '0'
                        queue.append((k - 1) * len(grid[0]) + r)
                    if k + 1 < len(grid) and grid[k + 1][r] == '1':
                        grid[k + 1][r] = '0'
                        queue.append((k + 1) * len(grid[0]) + r)
                    if r - 1 >=0 and grid[k][r - 1] == '1':
                        grid[k][r - 1] = '0'
                        queue.append(k * len(grid[0]) + (r - 1))
                    if r + 1 < len(grid[0]) and grid[k][r+1] == '1':
                        grid[k][r + 1] = '0'
                        queue.append(k * len(grid[0]) + (r + 1))
        return total

if __name__ == "__main__":
    s = Solution()
    s.numIslands([["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]])