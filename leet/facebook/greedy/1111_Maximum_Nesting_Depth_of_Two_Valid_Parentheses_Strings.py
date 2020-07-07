from typing import List

# this is genius
class Solution:
    '''
    We actually want to split the set of brakets into two subsequence
    with the mininmum possible max nesting value
    Natural approach to this is using modulo 2
    Even nested braket will fall under A
    Odd nested braket will fall under B
    '''
    def maxDepthAfterSplit(self, seq: str) -> List[int]:
        balance = 0
        res = []
        for c in seq:
            _open = c == '('
            if _open:
                balance += 1
            res.append(balance % 2)
            if not _open:
                balance -= 1
        return res



class SolutionMy:
    def maxDepthAfterSplit(self, seq: str) -> List[int]:
        balance = 0
        res = [0] * len(seq)
        maxbal = 0
        for ch in seq:
            if ch == '(':
                balance += 1
            else:
                balance -= 1
            maxbal = max(maxbal, balance)

        balA = maxBalA = maxbal // 2
        balB = maxBalB = maxbal - balA

        for i, ch in enumerate(seq):
            if ch == '(':
                if balA > 0:
                    res[i] = 0
                    balA -= 1
                else:
                    res[i] = 1
                    balB -= 1
            else:
                if balA < maxBalA:
                    balA += 1
                    res[i] = 0
                else:
                    res[i] = 1
                    balB += 1

        return res


