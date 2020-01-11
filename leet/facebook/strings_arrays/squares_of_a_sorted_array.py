# https://leetcode.com/problems/squares-of-a-sorted-array/

class Solution(object):
    def sortedSquares(self, A):
        return sorted(x*x for x in A)