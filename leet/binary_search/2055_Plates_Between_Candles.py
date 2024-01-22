from bisect import bisect_left, bisect


class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:

        candles = []
        pref = [0]

        stack = []
        prev_candle_indes = None
        cnt = 0
        for i, ch in enumerate(s):
            if ch == '|':
                candles.append(i)
                if prev_candle_indes is not None:
                    pref.append(pref[-1] + cnt)
                prev_candle_indes = i
                cnt = 0
            else:
                cnt += 1
        # print(candles)
        # print(pref)
        res = []
        for i, j in queries:
            start = bisect_left(candles, i)
            end = bisect.bisect_right(candles, j) - 1
            if start < end:
                res.append(pref[end] - pref[start])
            else:
                res.append(0)

        return res