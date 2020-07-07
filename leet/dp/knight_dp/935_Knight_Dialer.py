class Solution1(object):
    moves = [(4, 6), (6, 8), (7, 9), (4, 8), (3, 9, 0), (), (1, 7, 0), (2, 6), (1, 3), (2, 4)]

    def knightDialer(self, N):
        return sum(self.knightDialer_(N, i) for i in range(10)) % (10 ** 9 + 7)

    def knightDialer_(self, N, i, dp={}):
        if N == 1: return 1
        if (N, i) not in dp:
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



