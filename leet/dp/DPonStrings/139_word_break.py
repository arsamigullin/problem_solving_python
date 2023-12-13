# Algo
# this is dp approach
# initially dp is filled with False except the first elemet
# then we use a well-known approach that checks every index from the beginning till the middle
from collections import deque
from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: list) -> bool:
        dp = [False] * (len(s) + 1)
        dp[0] = True
        d = {w:1 for w in wordDict}
        for i in range(1, len(s) + 1):
            for j in range(i):
                print(s[j:i])
                if dp[j] and s[j:i] in d:
                    dp[i] = True
                    break
        return dp[-1]



# Important to sort wordDict because we can inroduce the check
# where once the nextstart is greater that the first word in sorted wordDict we can break
# if the wordDict wouldn't be sorted we would have to traverse the entire array

# another important thing here is d
# if d[i] == True this means since the word wordDict[i] we cannot proceed further, i.e. no way to get other words
# either because the wordDict exhausted or because nextstart is greater that the length of initial string
class SolutionDFS:

    def wordBreak(self, s, wordDict):
        l = len(s)
        d = [False] * l
        di = sorted(wordDict, key = len)

        def _wordBreak(start):
            if d[start]:
                return False

            for w in di:
                nextstart = start + len(w)
                if nextstart > l:
                    break
                if s.startswith(w, start):
                    if nextstart == l or _wordBreak(nextstart):
                        return True
            d[start] = True
            return False

        return _wordBreak(0)

# The same as above but more clean solution
class SolutionDFS1:

    def wordBreak(self, s, wordDict):
        wordDict.sort(key=len)
        # we have dp to keep track on visited start position
        # once the word s reached the length
        dp = [None] * len(s)
        def helper(start):
            if dp[start] is None:
                for w in wordDict:
                    next_start = start + len(w)
                    if s.startswith(w, start):
                        if next_start == len(s) or helper(next_start):
                            dp[start] = True
                            break
                else:
                    dp[start] = False
            return dp[start]
        return helper(0)

# recursion with memoization
# O(n^3)
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        wordDict = set(wordDict)
        n = len(s)
        memo = {}

        def helper(i):
            if i >= n:
                return True
            if i not in memo:
                for j in range(i, n + 1):
                    if s[i:j] in wordDict:
                        if helper(j):
                            memo[i] = True
                            break
                else:
                    memo[i] = False
            return memo[i]

        return helper(0)

# BFS O(n^3)
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        q = deque()
        q.append(0)
        wordDict = set(wordDict)
        visited = set()
        while q:
            start = q.popleft()
            if start in visited:
                continue
            for i in range(start + 1, len(s) + 1):
                if s[start:i] in wordDict:
                    q.append(i)
                    if len(s) == i:
                        return True
            visited.add(start)

        return False

# DP O(n^3)
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True
        wordDict = set(wordDict)
        for i in range(n + 1):
            for j in range(i):
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
        return dp[-1]


if __name__ == "__main__":
    s = SolutionDFS1()
    s.wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"])