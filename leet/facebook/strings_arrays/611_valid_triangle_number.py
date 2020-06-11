from typing import List

# [3, 19, 22, 24, 35, 82, 84]

class Solution:
    '''
        consider this example
        [3, 19, 22, 24, 35, 82, 84]
        we start from 84(index is 5) and see if we have two numbers to the left of index 5 such that
        their sum greater than 84 (using binary search) where hi is i-1 and lo is 0
        In our case those numbers are 3 and 82 (3+82>84)
    '''
    def triangleNumber(self, nums: List[int]) -> int:
        res = 0
        n = len(nums)
        nums = sorted(nums)
        for i in range(n - 1, 1, -1):
            target = nums[i]
            lo = 0
            hi = i - 1
            while lo < hi:
                if nums[lo] + nums[hi] > target:
                    res += hi - lo
                    hi -= 1
                else:
                    lo += 1
        return res


class Solution:
    def triangleNumber(self, A: List[int]) -> int:
        A.sort()
        n,ans=len(A),0
        for k in reversed(range(n)):
            i=0
            for j in reversed(range(k)):
                while i<j and A[i]+A[j]<=A[k]:
                    i+=1
                if j-i>0:
                    ans+=j-i
        return ans


class Solution1:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()

        def binary_search(start, target):
            lo = start
            hi = len(nums)

            while lo < hi:
                mid = (lo + hi) // 2  # lo + (hi-lo)//2
                if target > nums[mid]:
                    lo = mid + 1
                else:
                    hi = mid
            return lo

        res = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                two_sides = nums[i] + nums[j]
                if j + 1 >= len(nums):
                    continue
                if nums[j + 1] >= two_sides:
                    continue
                index = binary_search(j + 1, two_sides)
                if index == len(nums) or nums[index] == two_sides:
                    index -= 1
                res += index - j
        return res


if __name__ == '__main__':
    s = Solution()
    s.triangleNumber([24,3,82,22,35,84,19])
    s.triangleNumber([1,1,3,4])
    s.triangleNumber([2,2,3,4])
