import collections
from typing import List


class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words.sort(key=len)
        d = collections.defaultdict(int)
        m = 1
        for word in words:
            for j in range(len(word)):
                child = word[:j] + word[j+1:]
                if child in d:
                    d[word] = max(d[child]+1, d[word])
                    m = max(m,d[word])
            d.setdefault(word,1)
        return m