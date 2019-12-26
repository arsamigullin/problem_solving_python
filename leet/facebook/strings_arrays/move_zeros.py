# 283 https://leetcode.com/problems/move-zeroes/

# I thinks this is quite tricky approach
class Solution1:
    def moveZeroes(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        i, j = 0, 1
        while i < len(nums):
            # since all zeros are going to be at the end we are skipping step if nums[i] !=0
            if nums[i] != 0:
                i += 1
                # there can situation where pointer i can be greater that pointer j, we need to align them
                # for example [1,2,3,0,2]
                if i >= j:
                    j = i + 1
                continue

            while j < len(nums):
                # controversially, if second pointer is pointing to 0 we want skipping this step
                if nums[j] == 0:
                    j += 1
                    continue
                # here the case where nums[i]==0 and nums[j]!=3
                nums[i], nums[j] = nums[j], nums[i]
                j += 1
                break
            i += 1
        return nums


class Solution:
    def moveZeroes(self, nums):
        i = 0
        j = 0
        while i < len(nums):
            if nums[i] == 0:
                i+=1
                continue
            nums[j], nums[i] = nums[i], nums[j]
            j+=1
            i+=1
        return nums


if __name__ == "__main__":
    s = Solution()
    s.moveZeroes([0, 1, 0, 3, 12])
