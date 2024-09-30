from typing import List


class Solution:
    def longestStrChain1(self, words: List[str]) -> int:

        n = len(words)
        words.sort(key=len)
        dp = [1] * n
        for i in range(n):
            for j in range(i):
                prev = words[j]
                cur = words[i]
                prev_i, cur_i = 0, 0
                cnt = 0
                if len(cur) - len(prev) != 1:
                    continue
                while prev_i < len(prev) and cur_i < len(cur):
                    if prev[prev_i] == cur[cur_i]:
                        prev_i += 1
                    cur_i += 1

                if prev_i == len(prev):
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)

    def longestStrChain(self, words: List[str]) -> int:

        n = len(words)
        words.sort(key=len)
        memo = {}

        def subsequence(i, j):
            cur = words[i]
            prev = words[j]
            if len(cur) - len(prev) != 1:
                return False
            cur_i, prev_i = 0, 0
            while cur_i < len(cur) and prev_i < len(prev):
                if cur[cur_i] == prev[prev_i]:
                    prev_i += 1
                cur_i += 1
            return prev_i == len(prev)

        def helper(i):
            if i >= n:
                return 0
            if i not in memo:
                memo[i] = 1
                for j in range(i + 1, n):
                    if subsequence(j, i):
                        memo[i] = max(memo[i], helper(j) + 1)
            return memo[i]

        res = 0
        for i in range(n):
            res = max(res, helper(i))
        return res


if __name__ == '__main__':
    s = Solution()
    s.longestStrChain(["a","b","ba","bca","bda","bdca"])
