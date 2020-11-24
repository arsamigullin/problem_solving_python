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

