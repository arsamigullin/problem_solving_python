class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:

        n = len(grid)
        m = len(grid[0])
        keys_set = set()
        lock_set = set()
        start_x, start_y = 0, 0
        all_keys = 0
        for i in range(n):
            for j in range(m):
                val = grid[i][j]
                if val in 'abcdef':
                    keys_set.add(val)
                    all_keys |= (1 << (ord(val) - ord('a')))
                elif val in 'ABCDEF':
                    lock_set.add(val)
                elif val == '@':
                    start_x = i
                    start_y = j

        print(all_keys)
        visited = defaultdict(set)
        visited[0].add((start_x, start_y))
        q = deque([(start_x, start_y, 0, 0)])  # x, y, collected keys, distance

        while q:
            x, y, keys, dist = q.popleft()
            for dx, dy in ((0, 1), (1, 0), (-1, 0), (0, -1)):  # [(0,1),(0,-1),(1,0),(-1,0)]:
                nx = x + dx
                ny = y + dy
                if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] != '#':
                    val = grid[nx][ny]
                    if val in keys_set and not ((1 << (ord(val) - ord('a'))) & keys):
                        new_keys = (1 << (ord(val) - ord('a')) | keys)
                        # If we collect all keys, return dist + 1.
                        # Otherwise, just add this state to seen and queue.
                        if new_keys == all_keys:
                            return dist + 1
                        visited[new_keys].add((nx, ny))
                        q.append((nx, ny, new_keys, dist + 1))


                        # NOTE we cannot do keys |= because we are in the loop. Doing so we modify keys
                        # keys |= (1<<(ord(val)-ord('a')))
                        # #print(keys)
                        # if keys == all_keys:
                        #     return dist + 1
                        # visited[keys].add((nx, ny))
                        # q.append((nx, ny, keys, dist + 1))
                    elif val in lock_set and not ((1 << (ord(val) - ord('A'))) & keys):
                        continue
                    elif (nx, ny) not in visited[keys]:
                        visited[keys].add((nx, ny))
                        q.append((nx, ny, keys, dist + 1))
        return -1