from typing import List

# A scientist has index h if h of his/her N papers have at least h citations each,
# and the other N − h papers have no more than h citations each.

# let's consider this array. i is paper and A[i] is citations count in that paper
# [0,1,3,5,6]
# here h index is 3 because paper with i = 2,3,4 has at least 3 citations (citations[2] has 3 citations
# citations[3] has 5 citations and citations[4] has 6 citations
# i.e. each of them has at least 3 citations

# this is more clear solution
class Solution:
    def hIndex(self, citations):

        n = len(citations)
        for idx, c in enumerate(citations):
            # if count of citation of the current paper idx is greater or equal the rest paper count
            if c >= n - idx:
                # we return that
                return n - idx
        return 0

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        N = len(citations)
        i = 0
        while i < N and citations[N-1-i] > i:
            i+=1
        return i

# binary search solution
class Solution:
    def hIndex(self, citations: List[int]) -> int:

        N = len(citations)
        lo = 0
        hi = N - 1
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if citations[mid] < N - mid:
                lo = mid + 1
            else:
                hi = mid
        if lo < N and citations[lo] == 0:
            return 0
        return N - lo

