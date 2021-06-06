

# smart solution
from typing import List


class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        if k ==n:
            return sum(cardPoints)
        currSum = sum(cardPoints[n-k:])
        maxSum = currSum
        i=0
        while i<k:
            currSum = currSum -cardPoints[n-k+i] +cardPoints[i]
            i+=1
            maxSum=max(maxSum,currSum)
        return maxSum


class SolutionMy:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        w = len(cardPoints) - k
        tot = sum(cardPoints)
        i, j = 0, w
        t = sum(cardPoints[:j])
        m = tot - t
        while j < len(cardPoints):
            t -= cardPoints[i]
            t += cardPoints[j]
            m = max(m, tot - t)
            i += 1
            j += 1
        return max(m, tot - t)
