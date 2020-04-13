import typing
List = typing.List
import collections

# this problem
#https://leetcode.com/problems/max-consecutive-ones-ii/

#find description in here
# max_consecutive_ones_III.py
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        i, ans = 0, 0
        cnt = collections.defaultdict(int)
        for j in range(len(nums)):
            cnt[nums[j]] += 1
            if j - i - cnt[1] >= 1:
                cnt[nums[i]] -= 1
                i += 1
            if j - i >= ans:
                ans = j - i + 1
        return ans


if __name__ == "__main__":
    s = Solution()
    s.findMaxConsecutiveOnes([0,0])
    s.findMaxConsecutiveOnes([1,1,0,1,0,1,1,1])
