
#https://leetcode.com/problems/partition-to-k-equal-sum-subsets/
import typing
List = typing.List
# 1 <= k <= len(nums) <= 16.
# 0 < nums[i] < 10000.

#Search by Constructing Subset Sums

# this and right below solutions are the same
# the difference is only how the recurcion breaks
# here if this condition if group + v <= target: is never met
# it just returns False
# if we reached the end of nums, it returns True
# this works because at the beginning we ensured that target is even number
class SolutionGroup(object):
    def canPartitionKSubsets(self, nums, k):
        target, rem = divmod(sum(nums), k)
        if rem: return False

        def search(groups):
            if not nums: return True
            v = nums.pop()
            for i, group in enumerate(groups):
                if group + v <= target:
                    groups[i] += v
                    if search(groups): return True
                    groups[i] -= v
                if not group: break
            nums.append(v)
            return False

        nums.sort()
        if nums[-1] > target: return False
        while nums and nums[-1] == target:
            nums.pop()
            k -= 1

        return search([0] * k)

# Algo
# 1. sort nums in reverse order
# 2. if first element > target, return False
# 3. initialize dp with length k. It represents k group where dp[ki] is current value at ki group
# as long as the i-value(of nums) fit into the particular group, i.e, (array[ki]+=nums[i])<=target we go deep
# and do the same for the rest values of nums
# 4. Once we reached the end of array and all elements in dp the same, i.e. len(set(dp)) == 1
# this means it is possible to split array into k subarrays
class SolutionDFS(object):
    def canPartitionKSubsets(self, nums, k):
	    target, m = divmod(sum(nums), k)
	    if m: return False
	    dp, n = [0]*k, len(nums)
	    nums.sort(reverse=True)
	    def dfs(i):
		    if i == n:
                # Having reached the end of array see if all elements in dp are the same
			    return len(set(dp)) == 1
		    for j in range(k):
			    dp[j] += nums[i]
                # it is important to have <= here since if dp[j] < than target we can try on others numbers from nums
			    if dp[j] <= target and dfs(i+1):
				    return True
			    dp[j] -= nums[i]
			    if not dp[j]: break
		    return False
	    return nums[0] <= target and dfs(0)


############Dynamic Programming on Subsets of Input##################




#top down

class SolutionDPTopDown(object):
    def canPartitionKSubsets(self, nums, k):
        target, rem = divmod(sum(nums), k)
        if rem or max(nums) > target: return False

        memo = [None] * (1 << len(nums))
        memo[-1] = True
        def search(used, todo):
            if memo[used] is None:
                # It turns out the maximum value that can be chosen so as to not cross a multiple of target, is targ = (todo - 1) % target + 1. 
                # This is essentially todo % target, plus target if that would be zero.
                targ = (todo - 1) % target + 1
                memo[used] = False
                for i, num in enumerate(nums):
                    if (used >> i) & 1 == 0 and num <= targ:
                        if  search(used | (1<<i), todo - num):
                            memo[used] = True
                            break

                #memo[used] = any(search(used | (1<<i), todo - num)
                                 #for i, num in enumerate(nums)
                                 #if (used >> i) & 1 == 0 and num <= targ)
            return memo[used]

        return search(0, target * k)


#Bottom-Up Variation

class SolutionBottomUp(object):
    def canPartitionKSubsets(self, nums, k):
        nums.sort()
        target, rem = divmod(sum(nums), k)
        if rem or nums[-1] > target: return False

        dp = [False] * (1 << len(nums))
        dp[0] = True
        total = [0] * (1 << len(nums))

        for state in range(1 << len(nums)):
            if not dp[state]: continue
            for i, num in enumerate(nums):
                future = state | (1 << i)
                if state != future and not dp[future]:
                    if (num <= target - (total[state] % target)):
                        dp[future] = True
                        total[future] = total[state] + num
                    else:
                        break
        return dp[-1]

if __name__ == "__main__":
    s=SolutionDPTopDown()
    #s.canPartitionKSubsets([4,3,2,3,5,2,1],4)
    #s.canPartitionKSubsets( [2,2,2,2,3,4,5],4)
    #s.canPartitionKSubsets([4,3,2,3,5,2,1],4)
    s.canPartitionKSubsets([6, 5, 5, 4],2)
