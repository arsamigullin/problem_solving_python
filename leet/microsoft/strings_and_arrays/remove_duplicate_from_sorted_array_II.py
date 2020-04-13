import typing
List = typing.List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        i, j = 1, 0
        cnt = 1
        prev = nums[0]
        while i < len(nums):
            if nums[i]!=prev:
                lim = min(2, cnt)
                nums[j:j+lim] = [prev]*lim
                prev = nums[i]
                cnt = 0
                j+=lim
            i+=1
            cnt+=1
        lim = min(2, cnt)
        nums[j:j + lim] = [prev] * lim
        j += lim
        return j



class Solution:
    '''
    here we move j only when cnt is less or equal 2
    and reset cnt once previous and current numbers are incorrect
    '''
    def removeDuplicates(self, nums: List[int]) -> int:
        i, j = 1, 1
        cnt = 1
        while i < len(nums):
            if nums[i] == nums[i - 1]:
                cnt += 1
            else:
                cnt = 1

            if cnt <= 2:
                nums[j] = nums[i]
                j += 1
            i += 1

        return j

if __name__ == "__main__":
    s=Solution()
    s.removeDuplicates([0,0,1,1,1,1,2,3,3])
