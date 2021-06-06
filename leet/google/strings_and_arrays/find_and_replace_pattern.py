from typing import List
# this problem
# https://leetcode.com/problems/find-and-replace-pattern/

# very very very similar problem
# https://leetcode.com/problems/isomorphic-strings/

class SolutionMy:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        res = []
        for word in words:
            cur = {ch: -1 for ch in pattern}
            wc = {ch: -1 for ch in word}
            isFound = True
            for i, (chw, chp) in enumerate(zip(word, pattern)):
                if wc[chw] == cur[chp]:
                    wc[chw] = i
                    cur[chp] = i
                else:
                    isFound = False
                    break
            if isFound:
                res.append(word)
        return res


class Solution(object):
    def findAndReplacePattern(self, words, pattern):
        res = []
        for word in words:
            found = True
            m1, m2 = {}, {}
            for w, p in zip(word, pattern):
                if w not in m1: m1[w] = p
                if p not in m2: m2[p] = w
                if (m1[w], m2[p]) != (p, w):
                    found = False
                    break
            if found:
                res.append(word)
        return res


class Solution:
    def findAndReplacePattern(self, words, p):
        def match(w):
            m1, m2 = {}, {}
            return all((m1.setdefault(i, j), m2.setdefault(j, i)) == (j, i) for i, j in zip(w, p))

        return filter(match, words)

if __name__ == "__main__":
    s = Solution()
    s.findAndReplacePattern(["abc","deq","mee","aqq","dkd","ccc"], "abb")

