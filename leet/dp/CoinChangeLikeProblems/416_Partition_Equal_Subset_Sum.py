# https://leetcode.com/problems/partition-equal-subset-sum/
# There are three options to solve the problem. All are quite effective

# 1. Dynamic Programming
# we store all the combinations of sum we visited
# let's consider example [1,5,5,11]
# the sum of the arr is 22, we create array of len 23
# in this array 1 means the sum (sum is index in this array) is found in this array
import collections
from typing import List


class Solution1:
    def canPartition(self, nums: list) -> bool:
        numSum = sum(nums)
        if numSum % 2 != 0:
            return False
        dp = [0] * (numSum + 1)
        dp[0] = 1 # this is to include number itself

        for num in nums:
            # for each number from range numSum .. 0
            # we check if dp[i] has been marked as 1
            # that means some of the number in nums sums up to i
            for i in range(numSum, -1, -1):
                if dp[i]:
                    dp[num + i] = 1 # mark the found sum sum
            if dp[numSum//2] == 1: # once we found the middle return True
                return True
        return False
# the same as above
class Solution2:
    def canPartition(self, nums: list) -> bool:
        numSum = sum(nums)
        if numSum % 2 != 0:
            return False
        target = numSum//2
        dp = [0] * (target + 1)
        dp[0] = 1 # this is to include number itself
        
        for num in nums:
            for i in range(target, num-1, -1):
                dp[i] += dp[i-num]
                if dp[target]>0:
                    return True
        return dp[target] > 0

# 2. this is using DFS approach.
# in considers array to be a graph
# let's consider example [1,3,5,5,8]
# the sum is 22 and half is 11. We want to find if we have elements that compose 11
# we sort array in reverse [8,5,5,3,1] and starting from the bigger node(number)
# in our case we do 11 - 8 on the first iteration and go deeper to check if the next item (which is 5) is less than 3
# it is not, and we put 3-5 = -2 to the memo with value 'False'
# so next time we do not need to calculate 5 again, we will just return False
# When reaching 3 we see that the difference is 0 (which means we that we have in the array numbers that compose target
# 11) we return True, since we initialized memo with {0:True}

# the goal is to find the target once

# why this works?
# if the solution exists, it will be found for a single pass, so the memo dict will be empty
# if the solution does not exist, memo will be filled with with False value for each key
class SolutionMemo:
    def canPartition(self, nums: list) -> bool:
        s, n, memo = sum(nums), len(nums), {0: True}
        if s & 1: return False
        nums.sort(reverse=True)
        def dfs(i, x):
            if x not in memo:
                memo[x] = False
                if x > 0:
                    for j in range(i, n):
                        if dfs(j+1, x-nums[j]):
                            memo[x] = True
                            # that is why break is here
                            break
            return memo[x]
            #s>>1 is the same as s//2
        return dfs(0, s >> 1)


class SolutionBits:
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        sum_val = 0
        bits = 1
        for num in nums:
            sum_val += num
            bits |= bits << num

        return (not sum_val % 2 == 1) and (bits >> (sum_val // 2)) & 1 == 1


class Solution4:
    def canPartition(self, nums: List[int]) -> bool:

        tot_sum = sum(nums)
        if tot_sum % 2 == 1:
            return False

        nums.sort(reverse=True)
        n = len(nums)
        memo = {}
        memo_cnt = collections.defaultdict(int)
        coll = []
        def helper(i, left):
            memo_cnt[i] += 1
            if left == 0:
                return True
            if left < 0:
                return False
            if i >= n:
                return False
            if i not in memo:
                for j in range(i, n):
                    coll.append((nums[j],j))
                    if helper(j + 1, left - nums[j]):
                        return True
                    coll.pop()
                memo[i] = False
            return memo[i]

        res = helper(0, tot_sum // 2)
        print(memo)
        print(coll)
        return res

if __name__ == "__main__":
    #s = SolutionBits()
    #s.canPartition([1,5,5,11])
    s = Solution4()
    s.canPartition([100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,99,97])
    # s.canPartition([1,5,5,11])
    # s = SolutionMemo()
    # s.canPartition([1,3,5,5,8])
    # s = Solution2()
    # s.canPartition([5,5,11,1])