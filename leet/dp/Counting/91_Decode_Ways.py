import collections


class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        if n<=0:
            return 0
        if s[0]  == '0':
            return 0
        prev = 1
        pprev = 0
        for i in range(1, n):
            cur = 0
            if 1<=int(s[i])<=9:
                cur = prev
            if 10<=int(s[i-1: i + 1])<=26:
                cur += 1 if i - 2< 0 else pprev
            pprev, prev = prev, cur
        return prev

    def numDecodings1(self, s: str) -> int:
        memo = collections.defaultdict(int)
        n = len(s)

        def helper(i):
            if i == n:
                return 1
            if i > n:
                return 0
            if i not in memo:
                if 1 <= int(s[i]) <= 9:
                    memo[i] += helper(i + 1)
                if 10 <= int(s[i: i + 2]) <= 26:
                    memo[i] += helper(i + 2)
            return memo[i]

        return helper(0)

