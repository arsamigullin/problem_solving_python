import typing
List = typing.List
class Solution:
    '''
    NOTE: this recursion
            def find(n):
            if n==0:
                return 0
            return n+find(n-1)
        is the same as
        len(nums)*(len(nums)+1)//2 - this is Gaussian formula
    '''
    def missingNumber(self, nums: List[int]) -> int:
        def find(n):
            if n==0:
                return 0
            return n+find(n-1)
        total = find(len(nums))
        return total - sum(nums)

class Solution:
    '''
    NOTE: this recursion
            def find(n):
            if n==0:
                return 0
            return n+find(n-1)
        is the same as
        len(nums)*(len(nums)+1)//2 - this is Gaussian formula
    '''
    def missingNumber(self, nums):

        expected_sum = len(nums)*(len(nums)+1)//2
        actual_sum = sum(nums)
        return expected_sum - actual_sum


class SolutionBS:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        lo = 0
        hi = len(nums)
        while lo < hi:
            mid = (lo+hi)//2
            if nums[mid] == mid:
                lo = mid + 1
            else:
                hi = mid
        return lo

class SolutionXOR:
    '''
    Because we know that nums contains nn numbers and that it is missing exactly one number on the range
    [0..n-1][0..n−1], we know that nn definitely replaces the missing number in nums.
    Therefore, if we initialize an integer to nn and XOR it with every index and value,
    we will be left with the missing number.
    Consider the following example (the values have been sorted for intuitive convenience, but need not be):
    '''
    def missingNumber(self, nums):
        missing = len(nums)
        for i, num in enumerate(nums):
            missing ^= i ^ num
        return missing

class Solution:
    def missingNumber(self, nums):
        num_set = set(nums)
        n = len(nums) + 1
        for number in range(n):
            if number not in num_set:
                return number

if __name__ == '__main__':
    s = SolutionXOR()
    s.missingNumber([0,2,3])