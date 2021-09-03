from functools import lru_cache

#O(n^2+n^2)
class Solution:
    def minimumDistance(self, word: str) -> int:
        n = len(word)
        memo = {}

        def get_dist(prev, cur):
            if prev is None:
                return 0
            prev_x, prev_y = divmod(ord(word[prev]) - ord('A'), 6)
            cur_x, cur_y = divmod(ord(word[cur]) - ord('A'), 6)
            return abs(prev_x - cur_x) + abs(prev_y - cur_y)

        def dfs(i, l, r):
            if i >= n:
                return 0
            if (i, l, r) not in memo:
                left = dfs(i + 1, i, r) + get_dist(l, i)
                right = dfs(i + 1, l, i) + get_dist(r, i)
                memo[(i, l, r)] = min(left, right)
            return memo[(i, l, r)]

        r = dfs(0, None, None)
        # print(memo)
        return r


class Solution1:
    def minimumDistance(self, word: str) -> int:
        def dist(n1, n2):
            if n1 is None:
                return 0
            x1, y1 = divmod(ord(n1) - ord('A'), 6)
            x2, y2 = divmod(ord(n2) - ord('A'), 6)
            return abs(x1 - x2) + abs(y1 - y2)

        @lru_cache(None)
        def two_fingers(i, l, r):
            if i == len(word):
                return 0
            n1 = dist(l, word[i]) + two_fingers(i + 1, word[i], r)
            n2 = dist(r, word[i]) + two_fingers(i + 1, l, word[i])
            return min(n1, n2)

        return two_fingers(0, None, None)
