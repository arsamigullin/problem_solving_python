from typing import List
from collections import Counter


class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        start = 0
        end = k
        n = len(nums)
        kdict = Counter(nums[:k])
        tot = sum(nums[:k])
        res = tot if len(kdict) == k else 0
        while end < n:
            kdict[nums[start]]-=1
            if kdict[nums[start]] == 0:
                kdict.pop(nums[start])
            kdict[nums[end]]+=1
            tot+=nums[end] - nums[start]
            if len(kdict) == k:
                res = max(res, tot)
            start+=1
            end+=1
        return res

if __name__ == '__main__':
    s = Solution()
    s.maximumSubarraySum([1,1,1,7,8,9], 3)