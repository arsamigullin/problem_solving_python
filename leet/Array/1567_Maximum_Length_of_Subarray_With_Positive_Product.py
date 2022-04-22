from typing import List


class Solution:
    def getMaxLen(self, nums: List[int]) -> int:

        pos = 0
        neg = 0
        tot = 0
        for n in nums:
            if n > 0:
                pos, neg = pos + 1, neg + 1 if neg > 0 else 0
            elif n < 0:
                pos, neg = neg + 1 if neg > 0 else 0, pos + 1
            else:
                pos, neg = 0, 0
            tot = max(tot, pos)
        return tot


class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        ans = pos = neg = 0
        for x in nums:
            if x > 0:
                pos, neg = 1 + pos, 1 + neg if neg else 0
            elif x < 0:
                pos, neg = 1 + neg if neg else 0, 1 + pos
            else:
                pos = neg = 0  # reset
            ans = max(ans, pos)
        return ans


class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        pos = 0
        neg = 0
        if nums[0] > 0:
            pos = 1
        if nums[0] < 0:
            neg = 1
        tot = pos
        for i in range(1, len(nums)):
            if nums[i] > 0:
                pos += 1
                neg = neg + 1 if neg > 0 else 0
            elif nums[i] < 0:
                pos, neg = neg + 1 if neg > 0 else 0, 1 + pos
            else:
                pos = 0
                neg = 0
            tot = max(pos, tot)
        return tot

if __name__ == '__main__':
    s = Solution()
    s.getMaxLen([1,-2,-3,4])