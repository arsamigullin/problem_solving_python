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


class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        if not s: return t
        xor = ord(s[0])
        for i in range(1, len(s)):
            xor ^= ord(s[i])
        for j in range(len(t)):
            xor ^= ord(t[j])
        return chr(xor)
