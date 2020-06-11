import collections
from typing import List


class Solution:
    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        color = [N] * (N + 1)

        graph = collections.defaultdict(list)
        for u, v in dislikes:
            graph[u].append(v)
            graph[v].append(u)

        q = collections.deque([(dislikes[0][0], 0)])
        while q:
            node, clr = q.popleft()
            if color[node] == N:
                color[node] = clr
            elif color[node] == clr:
                continue
            else:
                return False
            for child in graph[u]:
                if color[child] == N:
                    q.append((child, clr ^ 1))
        return True

if __name__ == '__main__':
    s = Solution()
    s.possibleBipartition(4, [[1,2],[1,3],[4,2],[4,3]])