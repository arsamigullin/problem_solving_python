import collections
from typing import List


class Solution:
    def diStringMatch(self, S: str) -> List[int]:
        q = collections.deque(range(len(S)+1))
        res = []
        for s in S:
            if s == 'I':
                res.append(q.popleft())
            else:
                res.append(q.pop())
        res.append(q.pop())
        return res


    def diStringMatch_Second_option(self, S: str) -> List[int]:
        s, l = 0, len(S)
        res = []
        for c in S:
            if c == "I":
                res.append(s)
                s += 1
            else:
                res.append(l)
                l -= 1
        res.append(s)
        return res