import collections


class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        c1 = collections.Counter(s)
        c2 = collections.Counter(t)
        return (c2 - c1).most_common()[0][0]


class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        c = collections.Counter(s)
        for ch in t:
            if ch not in c:
                return ch
            c[ch]-=1
            if c[ch] == 0:
                c.pop(ch)