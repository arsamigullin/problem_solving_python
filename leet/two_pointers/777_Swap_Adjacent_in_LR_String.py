# the good explanation is here
# https://leetcode.com/problems/swap-adjacent-in-lr-string/discuss/1536718/Python-Check-their-positions-with-Picture-Clean-and-Concise
# Two cases are worth to consider
# 1. start = XXXL end = LXXX
# 2. start = RXXX end XXXR
# in the first case, we can transform start to end by swapping XL in start multiple times
# that means L in start should be located to the right of L in end, meaning index L in start should >= index L in end

# the same logic for the seconde case, the only difference is RX is always going to the right
class Solution:
    def canTransform(self, start: str, end: str) -> bool:

        if start.replace('X', '') != end.replace('X', ''):
            return False
        n = len(start)
        loL = [i for i in range(n) if start[i] == 'L']
        hiL = [i for i in range(n) if end[i] == 'L']
        loR = [i for i in range(n) if start[i] == 'R']
        hiR = [i for i in range(n) if end[i] == 'R']

        for i, j in zip(loL, hiL):
            if j > i:
                return False

        for i, j in zip(loR, hiR):
            if j < i:
                return False

        return True


# misterious working solution
class Solution:
    def canTransform(self, start: str, end: str) -> bool:

        x = 'X'
        r = 'R'
        l = 'L'

        n = len(start)
        j = 0
        for i in range(n):
            ch = start[i]
            if ch != x:
                while j < n and end[j] == x:
                    j += 1
                if j == n:
                    return False
                if ch != end[j] or ch == r and j < i or ch == l and j > i:
                    return False
                j += 1
        while j < n:
            if end[j] != x:
                return False
            j += 1
        return True

if __name__ == '__main__':
    s = Solution()
    s.canTransform("RXXLRXRXL", "XRLXXRRLX")
    s.canTransform("XXXXXLXXXX", "LXXXXXXXXX")
