import collections
from typing import List


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        if not image:
            return image
        startColor = image[sr][sc]
        n = len(image)
        m = len(image[0])
        q = collections.deque([(sr, sc)])
        while q:
            x, y = q.popleft()
            if image[x][y] == newColor:
                continue
            image[x][y] = newColor
            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                r, c = dr + x, dc + y
                if 0 <= r < n and 0 <= c < m and image[r][c] == startColor:
                    q.append((r, c))
        return image
