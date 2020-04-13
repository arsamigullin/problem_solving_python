import typing
List = typing.List

# this running 408
# is while
class SolutionMy:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        cnt = 0
        i, j = 0, 0
        m = 0
        while j < len(nums):
            if nums[j] == 1:
                cnt += 1
            if j - i + 1 != cnt:
                i = j + 1
                m = max(m, cnt)
                cnt = 0
            j += 1
        return max(m, cnt)

# this is running 364 ms
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_ones, curr_ones = 0, 0
        for num in nums:
            if num == 1:
                curr_ones += 1
            else:
                max_ones = max(max_ones, curr_ones)
                curr_ones = 0
        return max(max_ones, curr_ones)

