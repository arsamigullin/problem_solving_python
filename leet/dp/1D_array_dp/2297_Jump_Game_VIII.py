import math
from typing import List


class Solution:
    def minCost(self, nums: List[int], costs: List[int]) -> int:

        def next_greater(arr):
            n = len(arr)
            result = [-1] * n
            stack = []
            for i in range(n):
                while stack and nums[stack[-1]] <= nums[i]:
                    index = stack.pop()
                    result[index] = i
                stack.append(i)
            return result

        def next_smaller(arr):
            n = len(arr)
            result = [-1] * n
            stack = []
            for i in range(n):
                while stack and nums[i] < nums[stack[-1]]:
                    index = stack.pop()
                    result[index] = i
                stack.append(i)
            return result

        greater = next_greater(nums)
        smaller = next_smaller(nums)
        n = len(nums)
        dp = [math.inf] * n
        dp[0] = 0
        for i in range(n):
            # dp[i] may be calculated by either greater or smaller
            # so we store this calculation in dp
            # and re-use it
            if greater[i] != -1:
                dp[greater[i]] = min(dp[greater[i]], dp[i] + costs[greater[i]])
            if smaller[i] != -1:
                dp[smaller[i]] = min(dp[smaller[i]], dp[i] + costs[smaller[i]])
        # print(greater)
        # print(smaller)
        # print(dp)
        return dp[-1]

if __name__ == '__main__':
    s = Solution()
    s.minCost([3,2,4,4,1], [3,7,6,4,2])
