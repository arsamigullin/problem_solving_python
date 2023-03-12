import collections
import math
from typing import List



class Solution:
    def maxSubarraySumCircular(self, A: List[int]) -> int:
        total = sum(A)
        totalMax = -math.inf
        totalMin = math.inf

        curMax = 0
        curMin = 0

        for num in A:
            curMax += num
            curMin += num

            if curMax > totalMax:
                totalMax = curMax
            if curMin < totalMin:
                totalMin = curMin

            if curMax < 0:
                curMax = 0
            if curMin > 0:
                curMin = 0

        if totalMax < 0:
            return totalMax
        else:
            return max(totalMax, total - totalMin)

class Solution1(object):
    def maxSubarraySumCircular(self, A):
        N = len(A)

        ans = cur = 0
        for x in A:
            cur = x + max(cur, 0)
            ans = max(ans, cur)

        # ans is the answer for 1-interval subarrays.
        # Now, let's consider all 2-interval subarrays.
        # For each i, we want to know
        # the maximum of sum(A[j:]) with j >= i+2

        # rightsums[i] = sum(A[i:])
        rightsums = [None] * N
        rightsums[-1] = A[-1]
        for i in range(N-2, -1, -1):
            rightsums[i] = rightsums[i+1] + A[i]

        # maxright[i] = max_{j >= i} rightsums[j]
        maxright = [None] * N
        maxright[-1] = rightsums[-1]
        for i in range(N-2, -1, -1):
            maxright[i] = max(maxright[i+1], rightsums[i])

        leftsum = 0
        for i in range(N-2):
            leftsum += A[i]
            ans = max(ans, leftsum + maxright[i+2])
        return ans


class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:

        n = len(nums)
        P = [0]
        for _ in range(2):
            for i in range(n):
                P.append(P[-1] + nums[i])

        # here we want to find max Pj-Pi such that j-n <= i < j
        # that means we do not want to sum subarray with the len more than n

        # this is to store i
        q = collections.deque([0])
        ans = nums[0]
        for j in range(1, len(P)):

            # q[0] is i here
            if q[0] < j - n:
                q.popleft()

            i = q[0]
            ans = max(ans, P[j] - P[i])

            while q and P[j] <= P[q[-1]]:
                q.pop()

            q.append(j)

        return ans


if __name__ == '__main__':
    s = Solution()
    s.maxSubarraySumCircular([5,-3,5])
    s.maxSubarraySumCircular([1,-2,3,-2])
