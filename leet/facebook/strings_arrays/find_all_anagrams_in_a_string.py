import collections
class Solution:
    def findAnagrams(self, s: str, p: str) -> list:
        LS = len(s)
        LP = len(p)
        S = 0
        P = 0
        A =  []
        if LP > LS: return []
        for i in range(LP):
            S, P = S + hash(s[i]), P + hash(p[i])
        if S == P:
            A.append(0)
        for i in range(LP, LS):
            S += (hash(s[i]) - hash(s[i-LP]))
            if S == P:
                A.append(i-LP+1)
        return A


class Solution:
    def findAnagrams(self, s: str, p: str) -> list:
        if len(p) > len(s):
            return []
        map_s = [0] * 26
        map_p = [0] *26
        for i in range(len(p)):
            map_s[ord(s[i]) - 97]+=1
            map_p[ord(p[i]) - 97]+=1
        c = []
        if map_s == map_p:
            c.append(0)
        for j in range(len(p), len(s)):
            map_s[ord(s[j]) - 97] +=1
            map_s[ord(s[j-len(p)]) - 97] -=1
            if map_s == map_p:
                c.append(j-len(p)+1)
        return c


if __name__ == "__main__":
    s=Solution()
    s.findAnagrams("acbab", "ab")