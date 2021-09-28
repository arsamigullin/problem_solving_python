from typing import List


class Solution:
    def minNumberOperations(self, A: List[int]) -> int:
        res = pre = 0
        for a in A:
            res += max(a - pre, 0)
            pre = a
        return res


# Segment tree solution
# https://leetcode.com/problems/minimum-number-of-increments-on-subarrays-to-form-a-target-array/discuss/757373/C%2B%2B-Segment-Tree-Solution-w-explanation-Accepted