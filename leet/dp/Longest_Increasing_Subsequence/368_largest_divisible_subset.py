from typing import List


class SolutionFast(object):
    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # The container that holds all intermediate solutions.
        # key: the largest element in a valid subset.
        subsets = {-1: set()}
        
        for num in sorted(nums):
            subsets[num] = max([subsets[k] for k in subsets if num % k == 0], key=len) | {num}
        
        return list(max(subsets.values(), key=len))


class SolutionRecursive:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        
        def EDS(i):
            """ recursion with memoization """
            if i in memo:
                return memo[i]
            
            tail = nums[i]
            maxSubset = []
            # The value of EDS(i) depends on it previous elements
            for p in range(0, i):
                if tail % nums[p] == 0:
                    subset = EDS(p)
                    if len(maxSubset) < len(subset):
                        maxSubset = subset
            
            # extend the found max subset with the current tail.
            maxSubset = maxSubset.copy()
            maxSubset.append(tail)
            
            # memorize the intermediate solutions for reuse.
            memo[i] = maxSubset
            return maxSubset
        
        # test case with empty set
        if len(nums) == 0: return []
        
        nums.sort()
        memo = {}
    
        # Find the largest divisible subset
        return max([EDS(i) for i in range(len(nums))], key=len)


class SolutionIterative(object):
    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if len(nums) == 0:
            return []

        # important step !
        nums.sort()
        
        # The container that keep the size of the largest divisible subset that ends with X_i
        # dp[i] corresponds to len(EDS(X_i))
        dp = [0] * (len(nums))
        
        """ Build the dynamic programming matrix/vector """
        for i, num in enumerate(nums):
            maxSubsetSize = 0
            for k in range(0, i):
                if nums[i] % nums[k] == 0:
                    maxSubsetSize = max(maxSubsetSize, dp[k])

            maxSubsetSize += 1
            dp[i] = maxSubsetSize
        
        """ Find both the size of largest divisible set and its index """ 
        maxSize, maxSizeIndex = max([(v, i) for i, v in enumerate(dp)])
        ret = []
        
        """ Reconstruct the largest divisible subset """ 
        # currSize: the size of the current subset
        # currTail: the last element in the current subset
        currSize, currTail = maxSize, nums[maxSizeIndex]
        for i in range(maxSizeIndex, -1, -1):
            if currSize == dp[i] and currTail % nums[i] == 0:
                ret.append(nums[i])
                currSize -= 1
                currTail = nums[i]
        
        return reversed(ret)



class ListNode:
    def __init__(self, val):
        self.next = None
        self.val = val

class SolutionMy:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        nums.sort()
        dp = [None] * len(nums)
        dp[0] = [1, ListNode(nums[0])]
        index_of_max = 0
        m = 0
        for i in range(1, len(nums)):
            for j in range(i):
                if dp[i] is None:
                    dp[i] = [1,ListNode(nums[i])]
                if nums[i]%nums[j]==0:
                    if dp[i][0]<dp[j][0] + 1:                  
                        dp[i][0] = dp[j][0] + 1
                        if m < dp[i][0]:
                            m = dp[i][0]
                            index_of_max = i
                        dp[i][1]= ListNode(nums[i]) 
                        dp[i][1].next = dp[j][1]
        node = dp[index_of_max][1]
        res = []
        while node:
            res.append(node.val)
            node = node.next
        
        return res


class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        nums.sort()
        res = []
        dp = [0] * len(nums)
        for i in range(len(nums)):
            dp[i] = []
            for j in range(i):
                if nums[i] % nums[j] == 0:
                    if len(dp[j]) > len(dp[i]):
                        dp[i] = dp[j][:]
            dp[i].append(nums[i])
            if len(dp[i]) > len(res):
                res = dp[i]
        return res
