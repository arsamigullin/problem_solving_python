# https://leetcode.com/problems/squares-of-a-sorted-array/

class Solution(object):
    def sortedSquares(self, A):
        return sorted(x*x for x in A)


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:

        n = len(nums)
        res = [0] * n

        i, j = 0, n - 1

        for k in range(n - 1, -1, -1):
            if abs(nums[i]) > abs(nums[j]):
                val = nums[i]
                i += 1
            else:
                val = nums[j]
                j -= 1
            res[k] = val ** 2

        return res