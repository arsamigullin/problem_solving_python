from typing import List


class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        tot = 0
        plus_i = 0
        # we can split A[i] + A[j] + i - j to A[i]+i and  A[j]-j
        # tot=8, plus_i=8, i=0, plus_i=8
        # tot=8, plus_i=8, i=1, plus_i=8
        # tot=11, plus_i=8, i=2, plus_i=8
        # tot=11, plus_i=8, i=3, plus_i=8
        # tot=11, plus_i=10, i=4, plus_i=10
        for i in range(len(values)):
            tot = max(tot, plus_i + values[i] - i) # this keeps track total and it should go first as here
            plus_i = max(plus_i, values[i] + i) # this keeps track A[i]+i
            print(f'tot={tot}, plus_i={plus_i}, i={i}, plus_i={plus_i}')
        return tot

    def maxScoreSightseeingPairSwapSignsThisIsWrong(self, values: List[int]) -> int:
        tot = 0
        plus_i = 0
        # we can split A[i] + A[j] + i - j to A[i]+i and  A[j]-j
        # tot=8, plus_i=8, i=0, plus_i=8
        # tot=10, plus_i=8, i=1, plus_i=8
        # tot=15, plus_i=8, i=2, plus_i=8
        # tot=15, plus_i=8, i=3, plus_i=8
        # tot=18, plus_i=8, i=4, plus_i=8
        for i in range(len(values)):
            tot = max(tot, plus_i + values[i] + i)  # this keeps track total and it should go first as here
            plus_i = max(plus_i, values[i] - i)  # this keeps track A[i]+i
            print(f'tot={tot}, plus_i={plus_i}, i={i}, plus_i={plus_i}')
        return tot

        return res

if __name__ == '__main__':
    s = Solution()
    s.maxScoreSightseeingPairSwapSignsThisIsWrong([8,1,5,2,6])
    s.maxScoreSightseeingPair([8,1,5,2,6])