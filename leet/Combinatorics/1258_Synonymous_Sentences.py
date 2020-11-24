import collections
from typing import List


class Solution:
    def generateSentences(self, synonyms: List[List[str]], text: str) -> List[str]:
        d = collections.defaultdict(str)

        for u, v in synonyms:
            d[u] = v
            d[v] = u

        index_list = []
        word_list = text.split()

        for i, word in enumerate(word_list):
            if word in d:
                index_list.append((i, word))

        res = []


        def helper(j, indexes):
            if j >= len(indexes):
                res.append(' '.join(word_list))
                return
            ind, cur = indexes[j]
            visited = set()
            while cur:
                if cur not in visited:
                    word_list[ind] = cur
                    visited.add(cur)
                    helper(j + 1, indexes)
                cur = d[cur]


        helper(0, index_list)
        return sorted(res)

if __name__ == '__main__':
    synonyms = [["a","QrbCl"]] # [["happy", "joy"], ["sad", "sorrow"], ["joy", "cheerful"]]
    text = "d QrbCl ya ya NjZQ" #"I am happy today but was sad yesterday"
    s = Solution()
    s.generateSentences(synonyms, text)