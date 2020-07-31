# string alignment problem also known as Edit distance
#
class Solution1:
    def minDistance(self, word1: str, word2: str) -> int:
        n = len(word1)
        m = len(word2)

        table = [[0 for _ in range(m + 1)] for _ in range(n + 1)]

        for i in range(1, n + 1):
            table[i][0] = -1 * i

        for i in range(1, m + 1):
            table[0][i] = -1 * i

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                left = table[i - 1][j] - 1
                down = table[i][j - 1] - 1
                left_down = table[i - 1][j - 1]
                if word1[i - 1] != word2[j - 1]:
                    left_down -= 1
                table[i][j] = max(left, down, left_down)

        return abs(table[n][m])


from collections import deque


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        visit, q = set(), deque([(word1, word2, 0)])
        while True:
            w1, w2, d = q.popleft()
            if (w1, w2) not in visit:
                if w1 == w2:
                    return d
                visit.add((w1, w2))
                while w1 and w2 and w1[0] == w2[0]:
                    w1, w2 = w1[1:], w2[1:]
                d += 1
                q.extend([(w1[1:], w2[1:], d), (w1, w2[1:], d), (w1[1:], w2, d)])