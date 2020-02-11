# the task is to sort the array that consists of only 0,1,2
# we use three pointers here
class Solution:
    def sortColors(self, nums: list) -> None:

        curr, f, s = 0, 0, len(nums) - 1
        while curr<=s:
            # if we met 2, put it to the end of an array
            if nums[curr] == 2:
                nums[curr], nums[s] = nums[s], nums[curr]
                # since we do not know what was under nums[s]
                # we move only s pointer
                s-=1
            elif nums[curr] == 0:
                nums[curr], nums[f] = nums[f], nums[curr]
                curr+=1
                f += 1
            else:
                curr+=1
