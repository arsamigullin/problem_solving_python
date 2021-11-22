import math
from functools import lru_cache

# this is the fastest solution
class Solution:
    def getMoneyAmount(self, n: int) -> int:
        return guess(1, n)

@lru_cache(None)
def guess(lo, hi):
    if lo >= hi:
        return 0
    # move mid between lo and hi and get max from both parts
    return min(i + max(guess(i + 1, hi), guess(lo, i - 1)) for i in range(lo, hi + 1))


class Solution:
    def getMoneyAmount(self, n: int) -> int:

        memo = {}

        def dp(lo, hi):
            if lo >= hi:
                return 0
            if (lo, hi) not in memo:
                min_val = math.inf
                for mid in range(lo, hi):
                    min_val = min(min_val, max(dp(lo, mid - 1), dp(mid + 1, hi)) + mid)
                memo[(lo, hi)] = min_val if min_val != math.inf else 0
            return memo[(lo, hi)]

        return dp(1, n)


if __name__ == '__main__':
    s = Solution()
    s.getMoneyAmount(10)