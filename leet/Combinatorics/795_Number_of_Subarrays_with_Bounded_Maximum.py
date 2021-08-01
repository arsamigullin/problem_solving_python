from typing import List


class Solution1:
    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:
        def count(bound):
            ans = 0
            cur = 0
            for a in nums:
                cur = cur + 1 if a <= bound else 0
                ans += cur
            return ans
        # the first call calcs all items that less or equal right. So we also have an answer for left doing this
        # the second call counts arrays that have nums less than left bound, so we exclude the arrays that does
        # not have left or right to be the maximum values
        return count(right) - count(left - 1)

class Solution:
    def numSubarrayBoundedMax(self, A: List[int], L: int, R: int) -> int:
        # Solution: https://leetcode.com/problems/number-of-subarrays-with-bounded-maximum/discuss/535154/CPP-O(N)-time-and-O(1)-space-with-explanation

        count = 0
        start = -1
        res = 0

        for i, element in enumerate(A):
            # we out of bound
            # reset everything
            if element > R:
                start = i
                count = 0
            # We within [L,R]
            elif element >= L:
                count = i - start
                res += count
            else:
                # element less than L
                res += count

        return res


# this is wrong
class Solution1:
    def numSubarrayBoundedMax(self, A: List[int], L: int, R: int) -> int:
        tot = 0
        i = 0
        while i < len(A):
            if L <= A[i] <= R:
                k, j = i - 1, i + 1
                count = 1
                cur = 0
                while (k >= 0 and A[k] <= R) or (j < len(A) and A[j] <= R):
                    if k >= 0 and A[k] <= R:
                        if count == 1:
                            cur += 1
                        else:
                            cur += count
                        count += 1
                        k -= 1
                    if j < len(A) and A[j] <= R:
                        if count == 1:
                            cur += 1
                        else:
                            cur += count
                        count += 1
                        j += 1
                tot += cur
                i = j
            else:
                i += 1
        return tot

if __name__ == '__main__':
    s = Solution()
    s.numSubarrayBoundedMax([2, 2, 1, 4, 3], 2, 3)
    s.numSubarrayBoundedMax([2, 1, 1, 1], 1, 2)
