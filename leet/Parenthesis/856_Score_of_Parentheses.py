import collections


class Solution:
    def scoreOfParentheses(self, S: str) -> int:
        i = 0
        bal = 0
        d = collections.defaultdict(int)

        while i < len(S):
            if S[i] == '(':
                bal += 1
                first = True
            else:
                if first:
                    d[bal] = 1
                d[bal - 1] += d[bal] * 2
                first = False
                d.pop(bal)
                bal -= 1
            i += 1
        return d[0] // 2
