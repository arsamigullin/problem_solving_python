import bisect
import math
from typing import List

class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        n = len(days)
        dp = [math.inf] * n
        for i in range(n):
            for c, d in zip(costs, [1,7,30]):
                prev_i = bisect.bisect_left(days, days[i] - d)
                if prev_i == i:
                    dp[i] = min(dp[i], c if prev_i <=0 else dp[i-1] + c)
                else:
                    dp[i] = min(dp[i], dp[prev_i]+c)
        print(dp)
        return dp[-1]





# binary search utilization
class Solution1:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:

        memo = {}
        n = len(days)

        def helper(i):
            if i >= n:
                return 0
            if i not in memo:
                memo[i] = math.inf
                for c, day in zip(costs, [1, 7, 30]):
                    next_i = bisect.bisect_left(days, days[i] + day)
                    memo[i] = min(memo[i], helper(next_i) + c)
            return memo[i]

        return helper(0)


class Solution2:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        d = {}

        def helper(i):
            if i >= len(days):
                return 0
            _min = float('inf')
            for day, c in zip([1, 7, 30], costs):
                if (i, c) not in d:
                    start = i
                    limit = days[start] + day
                    while start < len(days) and days[start] < limit:
                        start += 1
                    print(f"{start} {c} {day}")
                    d[(i, c)] = helper(start) + c
                _min = min(_min, d[(i, c)])
            return _min

        return helper(0)


if __name__ == '__main__':
    s = Solution()
    print(s.mincostTickets([1,5,8,9,10,12,13,16,17,18,19,20,23,24,29], [3,12,54]))
    print(s.mincostTickets([1, 4, 6, 7, 8, 20], [2, 7, 15]))
    print(s.mincostTickets([1, 4, 6, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 20, 21, 22, 23, 27, 28], [3, 13, 45]))
    print(s.mincostTickets([1, 2, 4, 5, 6, 9, 10, 12, 14, 15, 18, 20, 21, 22, 23, 24, 25, 26, 28], [3, 13, 57]))

