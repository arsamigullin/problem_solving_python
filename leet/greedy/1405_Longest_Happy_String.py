# microsoft
class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:

        s = [[a, 'a'], [b, 'b'], [c, 'c']]
        res = []
        while True:
            # note we sort here, the greater numbers are at the end
            s.sort()
            # if the res already has last two chars, we want to choose the ch with the largest count
            last = 1 if len(res) > 1 and res[-1] == res[-2] == s[-1][1] else 2
            if s[last][0]:
                res.append(s[last][1])
                s[last][0] -= 1
            else:
                break
        return ''.join(res)