# there is some similarity with find_all_numbers_disappeared_in_an_array.py
# Algo
# we iterate over the array
# and find the index we will negate the number at
# if the number at index is already negative
# add the number at i (NOT INDEX) to the res

class Solution:
    def findDuplicates(self, nums: list) -> list:
        res = []
        for i in range(len(nums)):
            index = abs(nums[i]) - 1
            if nums[index] > 0:
                nums[index] *= -1
            else:
                res.append(abs(nums[i]))
        return res

if __name__ == "__name__":
    s = Solution()
    s.findDuplicates([4,3,2,7,8,2,3,1])
