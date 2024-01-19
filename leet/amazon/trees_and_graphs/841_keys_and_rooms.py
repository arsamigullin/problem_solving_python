from typing import List


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:

        n = len(rooms)
        q = deque()
        q.append(0)
        count = 0
        visited = {0}
        while q:
            node = q.popleft()
            count += 1
            for ch in rooms[node]:
                if ch not in visited:
                    q.append(ch)
                    visited.add(ch)

        return count == n

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:

        visited = set()

        def dfs(node):
            if node in visited:
                return
            visited.add(node)
            for child in rooms[node]:
                dfs(child)

        dfs(0)
        return len(visited) == len(rooms)