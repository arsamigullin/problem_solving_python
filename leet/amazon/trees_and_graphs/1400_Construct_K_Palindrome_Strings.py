import collections


class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        # if the input string is shorter than the needed count k
        # it is impossible to construct k palindromes using ALL chars of s
        if len(s)<k:
            return False
        c = collections.Counter(s)
        # but if count of odd count of char is less or equal k
        # then we can construct
        return sum(1 for v in c.values() if v%2==1)<=k