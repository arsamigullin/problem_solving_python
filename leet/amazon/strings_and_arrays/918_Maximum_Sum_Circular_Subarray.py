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
# Let's suppose the input array is of size N
# this 1 <= j-i <= N means to keep window of N size because the subarray cannot be greater than N
# here is possible values for i and j if N = 3
# j i
# 2 0
# 2 1
# 3 0
# 3 1
# 3 2
# 4 1
# 4 2
# 4 3
# 5 2
# 5 3
# 5 4
# 6 3
# 6 4
# 6 5


        # Compute P[j] = sum(B[:j]) for the fixed array B = A+A
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
            # If the smallest i is too small, remove it.
            if deque[0] < j-N:
                deque.popleft()

            # q[0] is i here
            if q[0] < j - n:
                q.popleft()

            # Remove any i1's with P[i2] <= P[i1].
            while deque and P[j] <= P[deque[-1]]:
                deque.pop()

            while q and P[j] <= P[q[-1]]:
                q.pop()

            q.append(j)

        return ans


if __name__ == '__main__':
    s = Solution2()
    s.maxSubarraySumCircular([1, -2, 3, -2])
    #s.maxSubarraySumCircular([5,-3,5])

