import collections
from typing import List

# TLE because the solution is nk where n is len of nums and 0<n,k<10**5
class SolutionTLE:
    def maxResult(self, nums: List[int], k: int) -> int:

        memo = collections.defaultdict(int)

        def helper(i):
            if i == len(nums) - 1:
                return nums[i]
            if i not in memo:
                max_score = float('-inf')
                for j in range(1, k + 1):
                    if i + j < len(nums):
                        max_score = max(max_score, helper(i + j) + nums[i])
                memo[i] = max_score

            return memo[i]

        return helper(0)


# monotonic decreasing deque
import heapq


from collections import  deque
class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        n = len(nums)
        score = [0]*n
        score[0] = nums[0]
        dq = deque()
        dq.append(0)
        '''      
        O(n)
        '''
        for i in range(1, n):
            # pop the old index
            # this loop will cut off all the elements whose index is less than i-k
            # so we always want to have at most k elements here, kind of window of k elements
            # and since this is  monotonic decreasing deque, the very first item is always element with the max value
            while dq and dq[0] < i-k:
                dq.popleft()
            score[i] = score[dq[0]] + nums[i]
            # pop the smaller value
            # this is what does the deque to be a monotonic decreasing
            # out of items nums[i-k] ... nums[i] we popping all items that is smaller than the current score[i]
            while dq and score[i] >= score[dq[-1]]:
                dq.pop()
            # and eventually we add the current one
            dq.append(i)
        return score[-1]


class SolutionPq:
    def maxResult(self, nums: List[int], k: int) -> int:
        n = len(nums)
        score = [0]*n
        score[0] = nums[0]
        priority_queue = []
        # since heapq is a min-heap,
        # we use negative of the numbers to mimic a max-heap
        '''
        O(NlogN)
        '''
        heapq.heappush(priority_queue, (-nums[0], 0))
        for i in range(1, n):
            # pop the old index
            while priority_queue[0][1] < i-k:
                heapq.heappop(priority_queue)
            score[i] = nums[i]+score[priority_queue[0][1]]
            heapq.heappush(priority_queue, (-score[i], i))
        return score[-1]


if __name__ == '__main__':
    s = Solution()
    s.maxResult([10,-5,-2,4,0,3],2)
    s.maxResult([1,2,5,3],2)