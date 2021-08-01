from typing import List
import bisect

# Conditions
# i<j<k
# nums[i]<nums[k]<num[j]


# O n^2
class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        mini = float('inf')

        for j in range(len(nums)):
            mini = min(mini, nums[j])
            for k in range(j + 1, len(nums)):
                if mini < nums[k] < nums[j]:
                    return True
        return False

# O n^2
class SolutionInterval:
    '''

    '''
    def find132pattern(self, nums: List[int]) -> bool:
        intervals = []
        i = 1
        s = 0
        while i < len(nums):
            # once we've found that nums[i] is less than nums[i-1]
            # in other words nums[k] < nums[j], where nums[k] is nums[i] and nums[j] is nums[i-1]
            if nums[i-1]>nums[i]:
                # we want to add this interval to the intervals
                # s<i-1 ensures that i < j where s is i and i-1 is j (this is one of the problem's condition)
                if s<i-1:
                    intervals.append((s, i-1))
                # this ensure that no intervals will be crossed
                # the start of the next interval is i
                s=i
            for a,b in intervals:
                if nums[a] < nums[i] <nums[b]:
                    return True
            i+=1
        return False

# O(n)
class SolutionOn:

    def find132pattern(self, nums: List[int]) -> bool:
        n = len(nums)
        mins = [0] * n
        mins[0] = nums[0]
        # we do pre processing
        # mins array contains the potential nums[i]
        for i in range(1, n):
            mins[i] = min(mins[i - 1], nums[i])

        stack = [] # stack stores nums[k] elements
        # since we start traversing from the end we are sure that k are greater than j
        for j in range(n - 1, -1, -1):
            # this gets rid of nums[k] that are less than nums[j]
            while stack and stack[-1] <= mins[j]:
                stack.pop()
            # if we have anything in the stack and its element less than num[j]
            # or in other words, if nums[k] items left in the stack and
            # and the latest one is less than nums[j] (which is one of the problem condition)
            # than means we have nums[i]<nums[k]<nums[j]
            # where nums[i] is mins[j], nums[k] is from stack and nums[j] is nums[j]
            # and also i<j<k
            if stack and stack[-1] < nums[j]:
                return True
            stack.append(nums[j])
        return False

# O NlgN
# interesting solution
class SolutionLog:
    def find132pattern(self, nums: List[int]) -> bool:
        n = len(nums)
        mins = [0] * n
        mins[0] = nums[0]
        # this is standard pre-processing
        # i.e. we find definde potential nums[i]
        for i in range(1, n):
            mins[i] = min(mins[i - 1], nums[i])

        k = n
        for j in range(n - 1, -1, -1):
            # if this true, then we want to find k
            if nums[j] > mins[j]:
                k = bisect.bisect_left(nums, mins[j] + 1, k, n)
                if k < n and nums[k] < nums[j]:
                    return True
                k -= 1
                nums[k] = nums[j]
        return False

if __name__ == '__main__':
    s = SolutionOn()
    s.find132pattern([3,1,4,2])
    s.find132pattern([5, 6, 4, 7, 3, 8, 2, 9])