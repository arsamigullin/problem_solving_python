from functools import lru_cache
from itertools import accumulate
from typing import List

# O(n^2)
class Solution:
    def stoneGameVII(self, stones: List[int]) -> int:
        n = len(stones)
        pref = [0] * (n + 1)
        for i in range(n):
            pref[i + 1] = pref[i] + stones[i]
        Alice = float('-inf')
        Bob = float('-inf')
        memo = {}

        def helper(i, j, turn):
            nonlocal Alice, Bob
            if i == j:
                return 0
            if (i, j) not in memo:
                # the score when choosing the left stone
                left = pref[j + 1] - pref[i + 1]
                # the score when choosing the right stone
                right = pref[j] - pref[i]
                # each time we sum/subtract the difference returned from the opposite player
                if turn == 1:
                    # when both helpers return 0, we will actually select max between left and right score
                    difference = max(helper(i + 1, j, turn ^ 1) + left, helper(i, j - 1, turn ^ 1) + right)
                else:
                    # we use min here to maximize the Bob's score
                    # the Bob's difference is negative
                    # when both helpers return 0, we will actually select min between left and right score
                    difference = min(helper(i + 1, j, turn ^ 1) - left, helper(i, j - 1, turn ^ 1) - right)
                memo[(i, j)] = difference
            return memo[(i, j)]

        return helper(0, n - 1, 1)

# O(n^2)
class Solution:
    def stoneGameVII(self, stones: List[int]) -> int:
        n = len(stones)
        pref = [0] * (n + 1)
        for i in range(n):
            pref[i + 1] = pref[i] + stones[i]
        memo = {}

        def helper(i, j, turn):
            if i == j:
                return 0
            if (i, j) not in memo:
                left = pref[j + 1] - pref[i + 1]
                right = pref[j] - pref[i]
                # each player to maximize the difference
                # that is why we return the max difference
                difference = max(left - helper(i + 1, j, turn ^ 1), right - helper(i, j - 1, turn ^ 1))
                memo[(i, j)] = difference
            return memo[(i, j)]

        return helper(0, n - 1, 1)


# O(n^2)
class Solution:
    def stoneGameVII(self, stones: List[int]) -> int:
        n= len(stones)
        pref=[0]*(n+1)
        for i in range(n):
            pref[i+1] = pref[i]+stones[i]
        dp= [[0]*n for _ in range(n)]
        for l in range(2, n+1):
            start = 0
            while start + l - 1 < n:
                end = start + l - 1
                left = pref[end+1] - pref[start+1]
                right = pref[end] - pref[start]
                dp[start][end] = max(left-dp[start+1][end],right-dp[start][end-1])
                start+=1
        return dp[0][n-1]


class Solution1:
    def stoneGameVII(self, stones: List[int]) -> int:
        n = len(stones)
        dp = [0] * n

        for i in range(n - 1, -1, -1):
            v = stones[i]
            run_sum = 0

            for j in range(i + 1, n):
                new_run = run_sum + stones[j]
                dp[j] = max(new_run - dp[j], run_sum + v - dp[j - 1])
                run_sum = new_run
        return dp[n - 1]


class Solution:
    def stoneGameVII(self, A):
        CSum = [0] + list(accumulate(A))

        @lru_cache(2000)
        def dp(i, j):
            if i > j: return 0
            sm = CSum[j + 1] - CSum[i]
            return sm - min(A[i] + dp(i + 1, j), A[j] + dp(i, j - 1))

        return dp(0, len(A) - 1)