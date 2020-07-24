class Solution:
    def numSubarrayProductLessThanK(self, nums: list, k: int) -> int:
        # this comes from requirements
        # 0<=k
        # 0<nums[i]
        # even if all numbers in nums are 1 their product will equal k (the problem states less than k)
        if k <= 1:
            return 0
        ans = left = 0
        product = 1
        for i, val in enumerate(nums):
            product *= val
            # once we got the product greater that k
            # we must get rid of the leftmost items
            while product >= k:
                product /= nums[left]
                left += 1
            ans += i - left + 1
        return ans


# https://leetcode.com/problems/subarray-product-less-than-k/solution/
import math
import bisect
class SolutionLg(object):
    def numSubarrayProductLessThanK(self, nums, k):
        if k == 0: return 0
        k = math.log(k)

        prefix = [0]
        # this is prefix sums
        for x in nums:
            prefix.append(prefix[-1] + math.log(x))

        ans = 0
        for i, x in enumerate(prefix):
            j = bisect.bisect(prefix, x + k - 1e-9, i+1)
            ans += j - i - 1
        return ans

if __name__ == "__main__":
    s = SolutionLg()
    s.numSubarrayProductLessThanK([10,5,2,6],100)