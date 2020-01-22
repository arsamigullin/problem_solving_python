# Algo
# this is dp approach
# initially dp is filled with False except the first elemet
# then we use a well-known approach that checks every index from the beginning till the middle


class Solution:
    def wordBreak(self, s: str, wordDict: list) -> bool:
        dp = [False] * (len(s) + 1)
        dp[0] = True
        for i in range(1, len(s) + 1):
            for j in range(i):
                print(s[j:i])
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
                    break
        return dp[-1]