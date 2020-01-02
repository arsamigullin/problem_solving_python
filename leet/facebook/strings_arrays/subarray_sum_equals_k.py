
# https://leetcode.com/problems/subarray-sum-equals-k/
from collections import defaultdict
class Solution:
    # prefix sum approach O(n^2)
    # TLE
    def subarraySum_Pref_sum(self, nums, k):
        prefix = [0] * (len(nums)+1)
        count = 0
        for i in range(1, len(prefix)):
            prefix[i] = prefix[i - 1] + nums[i-1]
        for i in range(0, len(prefix)-1):
            for j in range(i+1, len(prefix)):
                if prefix[j] - prefix[i] == k:
                    count +=1
        return count
    # here we just using cumulative _sum starting from 0
    # the idea is if the sum up
    # upto two indices is the same, the sum of the elements lying in between those indices is zero.
    # for example [2,3,-3,1,2], sum up to index 1 is 5 and sum up to index 4 is 5 also,
    # so the sum of subarray from index 2 to index 4 is -3 + 1 + 2 =0
    # The same idea with k. If difference between sums up to two different indices is k,
    # the we can subtract k from sum up some index and try to find difference in hash map.
    # if we found the second sum that means we found that subarray
    def subarraySum(self, nums, k):
        d = defaultdict(int)
        d[0]=1
        _sum = 0
        count = 0
        for i in range(len(nums)):
            _sum+=nums[i]
            if _sum - k in d:
                count += d[_sum - k]
            d[_sum]+=1
        return count



if __name__ == "__main__":

    s = Solution()
    #s.subarraySum([2,3,-3,1,2],5)
    s.subarraySum([1,1,1], 2)
    s.subarraySum([-1,-1,1],2)
    s.subarraySum([1,2,3],3)
    s.subarraySum([1,2,1,2,1], 3)
