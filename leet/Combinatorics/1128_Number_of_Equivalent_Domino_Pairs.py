import collections
from typing import List


class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        d = collections.defaultdict(int)
        for a, b in dominoes:
            s = tuple(sorted([a, b]))
            d[s] += 1

        tot = 0
        for (a, b), count in d.items():
            tot += (count * (count - 1)) // 2
        return tot