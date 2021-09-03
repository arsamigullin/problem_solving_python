import collections
from typing import List


class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        d = collections.defaultdict(int)

        def helper(i, j, turn=0):
            '''
            Alex and Lee would try to get the max pile
            Since Alex starts first he examines the game result when he takes pile[i] and pile[j] at
            each iteration

            The same do Lee. But he would subract the found
            '''
            if (i, j) in d:
                return d[(i, j)]
            if i > j:
                return 0
            # Alex's turn
            if turn == 0:
                res = max(piles[i] + helper(i + 1, j), piles[j] + helper(i, j - 1))
            # Lee's turn
            else:
                res = min(-piles[i] + helper(i + 1, j, turn ^ 1), -piles[j] + helper(i, j - 1, turn ^ 1))
            d[(i, j)] = res
            return res

        return helper(0, len(piles) - 1) > 0

class Solution1:
    def stoneGame(self, piles: List[int]) -> bool:
        d = collections.defaultdict(int)

        def helper(i, j, turn=0):
            '''
            Alex and Lee would try to get the max pile
            Since Alex starts first he examines the game result when he takes pile[i] and pile[j] at
            each iteration

            The same do Lee. But he would subract the found
            '''
            if (i, j) in d:
                return d[(i, j)]
            if i > j:
                return 0
            # Alex's turn
            if turn == 0:
                l = piles[i] + helper(i + 1, j)
                r = piles[j] + helper(i, j - 1)
                print(f'A: i+1={i+1} picked, result {l}')
                print(f'A: j-1={j-1} picked, result {r}')
                res = max(l, r)
            # Lee's turn
            else:
                l = -piles[i] + helper(i + 1, j, turn ^ 1)
                r = -piles[j] + helper(i, j - 1, turn ^ 1)
                print(f'L: i+1={i+1} picked, result {l}')
                print(f'L: j-1={j-1} picked, result {r}')
                res = min(l,r)
            d[(i, j)] = res
            return res

        return helper(0, len(piles) - 1) > 0


class Solution2:
    def stoneGame(self, piles: List[int]) -> bool:

        d = {}
        ares = 0
        lres = 0
        n = len(piles)

        def dfs(i, j, player):
            if i > j:
                return 0
            if (i, j) not in d:
                if player == 'a':
                    l = piles[i] + dfs(i + 1, j,'l')
                    r = piles[j] + dfs(i, j - 1,'l')
                    print(f'A: {(i+1,j)} picked, result {l}')
                    print(f'A: {(i,j-1)} picked, result {r}')
                    res = max(l, r)
                else:
                    l = -piles[i] + dfs(i + 1, j, 'a')
                    r = -piles[j] + dfs(i, j - 1, 'a')
                    print(f'L: {(i+1,j)} picked, result {l}')
                    print(f'L: {(i,j-1)} picked, result {r}')
                    res = min(l, r)
                d[(i, j)] = res
            return d[(i, j)]

        dfs(0, n - 1, 'a')

        return d[(0, n - 1)] > 0


if __name__ == '__main__':
    s = Solution2()
    s.stoneGame([5,3,4,5])