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


class Solution1:
    def findAnagrams(self, s: str, p: str) -> list:
        if len(p) > len(s):
            return []
        st = 'qwertyuiopasdfghjklzxcvbnm'
        dic = {}
        word = {}
        n = len(p)
        for w1 in st:
            dic[w1] = 0
            word[w1] = 0
        for w2 in p:
            dic[w2] += 1
        for i in range(n):
            word[s[i]] +=1
        c = []
        if word == dic:
            c.append(0)
        for j in range(n, len(s)):
            word[s[j]] +=1
            word[s[j-n]] -=1
            if word == dic:
                c.append(j-n+1)
        return c


if __name__ == "__main__":
    s=Solution()
    s.findAnagrams("acbab", "ab")