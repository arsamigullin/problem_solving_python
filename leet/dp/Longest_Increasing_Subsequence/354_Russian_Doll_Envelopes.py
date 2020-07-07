from typing import List


class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        if not envelopes:
            return 0
        n = len(envelopes)
        dp = [[0,0]] * n
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        l = 0
        for i in range(n):
            fw, fh = envelopes[i]
            lo = 0
            hi = l
            while lo < hi:
                mid = lo + (hi - lo) // 2
                sw, sh = dp[mid]
                if fw > sw and fh > sh:
                    lo = mid + 1
                else:
                    hi = mid
            dp[lo] = envelopes[i]
            if lo == l:
                l += 1
        return l

if __name__ == '__main__':

    s = Solution()
    s.maxEnvelopes([[2,100],[3,200],[4,300],[5,500],[5,400],[5,250],[6,370],[6,360],[7,380]])
    s.maxEnvelopes([[4, 5], [4, 6], [6, 7], [2, 3], [1, 1], [1, 1]])
    s.maxEnvelopes([[5,4],[6,4],[6,7],[2,3]])
