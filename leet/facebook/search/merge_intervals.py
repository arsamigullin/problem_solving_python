# Algo
# 1. Sort by first start time of intervals
# 2. if end of current intervals is greater or equal the start of the next interval
#   take the maximum time of these intervals
#   otherwise this is new interval
class Solution:
    def merge(self, intervals: list) -> list:
        if intervals is None or len(intervals) == 0:
            return []
        intervals = sorted(intervals, key=lambda k: k[0])
        res = []
        for i in range(len(intervals)):
            s, e = intervals[i]
            if not res or res[-1][1] < e:
                # this is a new interval
                res.append([s,e])
            else:
                # update end of interval
                res[-1][1] = max(res[-1][1], e)
        return res