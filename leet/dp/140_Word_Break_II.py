import collections
from typing import List

class Word:
    def __init__(self):
        self.done = False
        self.words = []


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        n = len(s)
        words = set(wordDict)
        memo = collections.defaultdict(Word)

        def dfs(i):
            if i >= n:
                w = Word()
                w.done = True
                return w
            if i not in memo:
                for j in range(i, n + 1):
                    if s[i:j] in words:
                        w = dfs(j)
                        if not w.done:
                            continue
                        memo[i].done = True
                        if len(w.words) == 0:
                            memo[i].words.append([s[i:j]])
                        else:
                            for lst in w.words:
                                memo[i].words.append([s[i:j]] + lst)
            return memo[i]

        dfs(0)
        return [' '.join(arr) for arr in memo[0].words]

if __name__ == '__main__':
    s =Solution()
    s.wordBreak("catsanddog", ["cat","cats","and","sand","dog"])
    s.wordBreak("catsanddog",["cat","cats","and","sand","dog"])