from functools import lru_cache
from typing import List

# O(n2)
class Solution1:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums)<3:
            return max(nums)
        dp = [0] * len(nums)
        dp[0] = nums[0]
        _max = 0
        for i in range(1, len(nums)):
            dp[i] = nums[i]
            for j in range(0, i - 1):
                dp[i] = max(dp[i], dp[j] + nums[i])
            _max = max(_max, dp[i])
        return _max
# O(n)


class Solution2:
    '''
    prevMax will be pointing to the a[i-2]
    curMax will be pointing to the a[i-1]
    let's consider this array
    [2,7,9,3,1]
    1 iteration
    prevMax = 0
    curMax = 2
    2 iter
    NOTE: prevMax is collected money from 0 to i-2 house
    that is why we check what is the max here
    prevMax + num or curMax (which is money collected from 0 to i-1)

    '''
    # 2 7 9 3 1
    # p, c = 0, 0
    # 2, 0
    # 0+7, 2
    # 2+9, 7
    # 7+3, 11
    # 11+1, 11
    # to keep the gap of 1 house
    # we assign to prevMax curMax
    # curMax is m
    def rob(self, nums: List[int]) -> int:
        curMax = 0
        prevMax = 0
        for num in nums:
            prevMax, curMax = curMax, max(prevMax + num, curMax)
        return curMax


class Solution:
    def rob(self, nums: List[int]) -> int:

        n = len(nums)
        if n <= 2:
            return max(nums)
        dp = [0] * n
        dp[0] = nums[0]
        dp[1] = nums[1]
        for i in range(2, n):
            dp[i - 1], dp[i] = max(dp[i - 1], dp[i - 2]), max(dp[i - 2] + nums[i], dp[i - 1])
        return dp[-1]


class Solution:
    def rob(self, nums: List[int]) -> int:

        memo = {}
        n = len(nums)

        def helper(i):
            if i >= n:
                return 0
            if i not in memo:
                memo[i] = max(helper(i + 2) + nums[i], helper(i + 1))
            return memo[i]

        return helper(0)

# O(n)
class Solution3(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d = [0] * (len(nums) + 1)
        total = 0
        for i in range(0, len(nums)):
            if i in (0, 1):
                d[i] = nums[i]
            elif i == 2:
                d[i] = d[0] + nums[i]
            else:
                d[i] += nums[i] + max(d[i - 2], d[i - 3])
            total = max(total, d[i])

        return total


class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        @lru_cache(None)
        def dp(i):
            if i >= n:
                return 0
            tot = nums[i]
            for j in range(i + 2, n):
                tot = max(tot, dp(j) + nums[i])
            return tot

        # return max(dp(0), dp(1))
        if n == 0:
            return 0
        if n == 1:
            return nums[0]
        first, sec = 0, 0
        for i in range(n):
            first, sec = max(sec + nums[i], first), first
        return max(first, sec)

if __name__ == '__main__':
    s = Solution2()
    s.rob([3,2,4,5,8])