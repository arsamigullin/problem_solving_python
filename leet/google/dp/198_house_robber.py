from typing import List

# O(n2)
class Solution:
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


class Solution:
    '''
    prevMax will be pointing to the a[i-2]
    curMax will be pointing to the a[i-1]
    let's consider this array
    [1,2,5,3,4]
    1 iteration
    curmax = 1
    prevmax = 0
    2 iteration
    curmax = max(1, 0 + 2) = 2
    prevmax = 1
    3 iteration
    curmax = max(2, 1 + 5) = 6
    prevmax = 2
    4 iteration
    curmax = max(6, 3 + 2) = 6
    prevmax = 6

    '''
    def rob(self, nums: List[int]) -> int:
        prevMax = 0
        curMax = 0
        for num in nums:
            temp = curMax
            curMax = max(prevMax+num, curMax)
            prevMax = temp
        return curMax

# O(n)
class Solution(object):
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
