import collections


class Solution1(object):
    # index of moves is the number on the dial pad
    # val is the numbers the knight can jump from index
    # from 0 the knight can jump to 4 and 6 and so on
    moves = [(4, 6), (6, 8), (7, 9), (4, 8), (3, 9, 0), (), (1, 7, 0), (2, 6), (1, 3), (2, 4)]

    def knightDialer(self, N):
        # range(10) - we want to try starting from every number on the dial pad
        return sum(self.knightDialer_(N, i) for i in range(10)) % (10 ** 9 + 7)

    def knightDialer_(self, N, i, dp={}):
        if N == 1: return 1
        if (N, i) not in dp:
            # self.knightDialer_(N - 1, j) - once knight jumped to the number j, the length of the target number
            # reduces to 1. We do so until we've got 1
            dp[(N, i)] = sum(self.knightDialer_(N - 1, j) for j in self.moves[i])
        return dp[(N, i)]


class Solution:
    def knightDialer(self, N: int) -> int:

        pad = [(4, 6), (6, 8), (7, 9), (4, 8), (3, 9, 0), (), (1, 7, 0), (2, 6), (1, 3), (2, 4)]
        tot = 0
        d = collections.defaultdict(int)

        def dfs(num, k):
            if k == 0:
                return 1
            if (num, k) in d:
                # print('here')
                return d[(num, k)]
            for x in pad[num]:
                if (x, k - 1) in d:
                    d[(num, k)] += d[(x, k - 1)]
                    # print('here')
                else:
                    d[(num, k)] += dfs(x, k - 1)
            return d[(num, k)]

        return sum(dfs(i, N - 1) for i in range(10)) % (10 ** 9 + 7)


class Solution4:
    def knightDialer(self, n: int) -> int:

        self.pad = [(4, 6), (8, 6), (7, 9), (4, 8), (0, 3, 9), (), (1, 7, 0), (2, 6), (1, 3), (2, 4)]
        MOD = 10 ** 9 + 7
        return sum(self.find(n, i) for i in range(10)) % MOD

    def find(self, N, i, d={}):
        if N == 1:
            return 1
        if (N, i) not in d:
            d[(N, i)] = sum(self.find(N - 1, j, d) for j in self.pad[i])
        return d[(N, i)]


class Solution5:
    def __init__(self):
        self.memo = {}

    def knightDialer(self, n: int) -> int:
        self.pad = [(4, 6), (8, 6), (7, 9), (4, 8), (0, 3, 9), (), (1, 7, 0), (2, 6), (1, 3), (2, 4)]
        self.count = 0
        MOD = 10 ** 9 + 7
        res = sum(self.find(n, i) for i in range(10)) % MOD
        return res

    def find(self, N, i):
        if N == 1:
            return 1
        if (N, i) not in self.memo:
            self.memo[(N, i)] = sum(self.find(N - 1, j) for j in self.pad[i])
        return self.memo[(N, i)]


if __name__ == '__main__':
    s = Solution5()
    s.knightDialer(4)