# this problem
# https://leetcode.com/problems/isomorphic-strings/
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        m1, m2 = {}, {}
        for w, p in zip(s, t):
            if w not in m1: m1[w] = p
            if p not in m2: m2[p] = w
            if (m1[w], m2[p]) != (p, w):
                return False
        return True