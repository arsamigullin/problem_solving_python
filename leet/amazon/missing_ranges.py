class Solution:
    def findMissingRanges(self, nums: list, lower: int, upper: int) -> list:
        i, res = 0, []
        nums = nums + [upper+1]
        while lower <= upper:
            if nums[i] > lower:
                if nums[i] - lower == 1:
                    res.append(str(lower))
                else:
                    res.append(str(lower) + '->' + str(nums[i]-1))
            lower, i = nums[i] + 1, i+1
        return res