
# this proble
# https://leetcode.com/problems/target-sum/

# similar problems
#https://leetcode.com/problems/expression-add-operators/
#https://leetcode.com/problems/partition-equal-subset-sum/

import typing
List = typing.List
# Algo
# Apply DFS
# 1. Define dp. The key for dp is key = i|sum_so_far
# 2. Value of each dp represents the count of ways to represent num S for index i and with sum so far at index i
# 3. To have the count of ways for a particular key we add the count of ways for add operation (+1) for subtract operation(-1)
class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        operations = [-1, 1]
        dp = {}
        def find(i,s):
            key = f"{i}|{s}"
            if key in dp:
                return dp[key]
            if i == len(nums):
                if s == S:
                    return 1
                else:
                    return 0
            add = find(i+1, s + nums[i])
            sub = find(i+1, s - nums[i])
            dp[key] = add + sub
            return dp[key]          
        return find(0, 0)



class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        operations = [-1, 1]
        dp = {}
        def find(i,s):
            key = f"{i}|{s}"
            if key in dp:
                return dp[key]
            if i == len(nums):
                if s == S:
                    return 1
                else:
                    return 0
            dp[key] = 0
            for k, op in enumerate(operations):
                sm = s + op * nums[i]
                res = find(i+1, sm)
                dp[key] += res
            return dp[key]          
        return find(0, 0)



# the approach from https://leetcode.com/problems/partition-equal-subset-sum/
# I do not understand how it is obtained from but it works
# Has to be revised later 
class SolutionFast:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        # the same as P416, just consider target as (S + sum(nums))//2
        # the problem becomes find the + numbers s.t the sum is target
        # the rest are assigned with - 
        if (S + sum(nums)) % 2 == 1 or S > sum(nums):
            return 0
        else:
            target = (S + sum(nums))//2
        dp = [0]*(target+1)      
        dp[0] = 1
        for num in nums:
            for j in range(target,num-1,-1):
                dp[j] += dp[j-num]
                
        return dp[target]

class SolutionShort:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        
        def dfs(cur, i, d = {}):
            if i < len(nums) and (i, cur) not in d: 
                d[(i, cur)] = dfs(cur + nums[i], i + 1) + dfs(cur - nums[i], i + 1)
            return d.get((i, cur), int(cur == S))
        
        return dfs(0, 0)

if __name__ == "__main__":
    s = SolutionFast()
    print(s.findTargetSumWays([1, 1, 1, 1, 1], 3))
    #s.findTargetSumWays([1], 1)
    #print(s.findTargetSumWays([43,1,49,22,41,1,11,1,24,10,26,49,33,4,20,19,44,42,2,37],17))
            