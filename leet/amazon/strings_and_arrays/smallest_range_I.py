# https://leetcode.com/problems/smallest-range-i/
class SolutionMy:
    def smallestRangeI(self, A: List[int], K: int) -> int:
        #Note: to have min and max values of array it is faster to do two separate min and max as opposed to sort!!!
        #A.sort()
        minA = min(A)
        maxA = max(A)
        if minA==maxA:
            return 0
        k1 = k2 = K
        
        while minA+k1>maxA-k2:
            k1-=1
        return maxA-k2 - (minA+k1)
        
class SolutionShort:
    def smallestRangeI(self, A: List[int], K: int) -> int:
        return max(0, max(A) - min(A) - 2*K)
        