from typing import List


class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        tot = 0
        plus_i = 0
        # we can split A[i] + A[j] + i - j to A[i]+i and  A[j]-j
        for i in range(len(values)):
            tot = max(tot, plus_i + values[i] - i) # this keeps track total
            plus_i = max(plus_i, values[i] + i) # this keeps track A[i]+i
        return tot

if __name__ == '__main__':
    s = Solution()
    s.maxScoreSightseeingPair()