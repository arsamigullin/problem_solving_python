import collections
import string
from typing import List


class Solution:  # 44 ms, faster than 86.16%
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        wordList = set(wordList)
        wordList.discard(beginWord)
        n = len(beginWord)
        layer = {beginWord: [[beginWord]]}

        # this just returns all neighbors
        # that differs to only one letter AND are in wordList
        # Note, we never return the w itself here because we
        # do clean up before
        def neighbors(w):
            for i in range(n):
                for c in string.ascii_lowercase:
                    nei = w[:i] + c + w[i + 1:]
                    if nei in wordList:
                        yield nei

        #
        while layer:
            new_layer = collections.defaultdict(list)
            for w, paths in layer.items():
                if w == endWord:
                    return paths
                # we go over the neighbors
                for nei in neighbors(w):
                    for p in paths:
                        # and add the nei to the existing path
                        # at some point two different words will have the same neighbor
                        # that is why this nei will have multiple paths
                        new_layer[nei].append(p + [nei])

            # this is clean up
            wordList -= new_layer.keys()
            layer = new_layer
        return []

if __name__ == '__main__':
    s = Solution()
    s.findLadders("hit", "cog", ["hot","dot","dog","lot","log","cog"])