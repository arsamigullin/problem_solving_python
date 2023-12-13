import math
from typing import List

class Solution:
    def minCost(self, nums: List[int], cost: List[int]) -> int:
        # nums[j]>=nums[i]>nums[k]
        # 1st case
        # i k k j
        # 5 4 3 5
        # 2nd case
        # i k k j
        # 5 5 5 3
        n = len(nums)
        dp = [math.inf] * n
        dp[0] = 0
        inc = []
        dec = []
        for i, num in enumerate(nums):
            while inc and nums[inc[-1]] <= num:
                dp[i] = min(dp[i], dp[inc.pop()] + cost[i])
            while dec and nums[dec[-1]] > num:
                dp[i] = min(dp[i], dp[dec.pop()] + cost[i])
            inc.append(i)
            dec.append(i)
        return dp[-1]


if __name__ == '__main__':
    s = Solution()
    s.minCost([3,2,4,4,1], [3,7,6,4,2])
