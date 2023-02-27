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

class Solution2(object):
    def maxSubarraySumCircular(self, A):
        N = len(A)

        # Compute P[j] = sum(B[:j]) for the fixed array B = A+A
        # cumulative sum
        P = [0]
        for _ in range(2):
            for x in A:
                P.append(P[-1] + x)

        # Want largest P[j] - P[i] with 1 <= j-i <= N
        # For each j, want smallest P[i] with i >= j-N
        ans = A[0]
        deque = collections.deque([0]) # i's, increasing by P[i]
        for j in range(1, len(P)):
            # If the smallest i is too small, remove it.
            # in other words if i went beyond N size window on the left side, we exclude it
            # because that i should not be used to find P[j]-P[i]
            if deque[0] < j-N:
                deque.popleft()

            # The optimal i is deque[0], for cand. answer P[j] - P[i].
            ans = max(ans, P[j] - P[deque[0]])

            # Remove any i1's with P[j] <= P[i].
            # if there P[i] that is greater or equal P[j]
            # we do not want to keep them because those won't contribute the max subarray
            # we want to keep smaller P[i], so the next P[j] subtracts smaller P[i]
            while deque and P[j] <= P[deque[-1]]:
                deque.pop()

            deque.append(j)

        return ans


if __name__ == '__main__':
    s = Solution2()
    s.maxSubarraySumCircular([1, -2, 3, -2])
    #s.maxSubarraySumCircular([5,-3,5])

