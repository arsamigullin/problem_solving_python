from typing import List


class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:

        s = set(words)
        res = []
        memo = {}

        # classical top-down
        def dp(i, j, n, w):
            if j >= n:
                return w[i:j + 1] != "" and w[i:j + 1] in s and i > 0
            if (i, j) not in memo:
                if w[i:j + 1] in s:
                    memo[(i, j)] = dp(j + 1, j + 1, n, w) or dp(i, j + 1, n, w)
                else:
                    memo[(i, j)] = dp(i, j + 1, n, w)
            return memo[(i, j)]

        for w in words:
            memo = {}
            if dp(0, 0, len(w), w):
                res.append(w)

        return res

if __name__ == '__main__':
    s = Solution()
    s.findAllConcatenatedWordsInADict(["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"])
