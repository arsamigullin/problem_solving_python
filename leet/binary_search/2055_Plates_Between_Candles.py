from bisect import bisect_left, bisect
from typing import List


class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:

        candles = []
        for i, ch in enumerate(s):
            if ch == '|':
                candles.append(i)

        # candles contains unique numbers
        res = []
        for i, j in queries:
            start = bisect_left(candles, i)
            end = bisect(candles, j) - 1
            if start < end:
                res.append(candles[end] - candles[start] - (end - start))
            else:
                res.append(0)

        return res

if __name__ == '__main__':
    s = Solution()
    s.platesBetweenCandles("*||***|||*",[[1,6]])