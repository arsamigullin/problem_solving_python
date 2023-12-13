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

        # we first find max subarray sum, that consists only of single intervals array
        ans = cur = 0
        for x in A:
            cur = x + max(cur, 0)
            ans = max(ans, cur)

        # ans is the answer for 1-interval subarrays.
        # Now, let's consider all 2-interval subarrays.
        # For each i, we want to know
        # the maximum of sum(A[j:]) with j >= i+2

        # rightsums[i] = sum(A[i:])

        '''
        explanation why we need j that is >= i+2. 
        this is because we need to create a gap
        finding max subarray sum on the entire array already covered in 1-interval subarrays
        suppose we have array [0,1,2,3,4,5]
        without having a gap it would be the same as to find max subarray sum for the 1-interval subarray        
        '''

        # here we just store cumulative sum starting from the right side
        rightsums = [None] * N
        rightsums[-1] = A[-1]
        for i in range(N-2, -1, -1):
            rightsums[i] = rightsums[i+1] + A[i]

        # maxright[i] = max_{j >= i} rightsums[j]
        maxright = [None] * N
        maxright[-1] = rightsums[-1]
        for i in range(N-2, -1, -1):
            maxright[i] = max(maxright[i+1], rightsums[i])

        # here we do sum left side and adding with max righ sum
        # NOTE: i+2 is what that creates a gap of 1 item
        # Suppose original array
        # [0, 1, -3, 1, 2, 1]
        # rightsums
        # [2, 2, 1, 4, 3, 1]
        # the maxright array
        # [4, 4, 4, 4, 3, 1]
        # NOTE: here in the maxright array under index 2 the value is 4, whereas cumulative sum
        # is rightsums is 1
        # 4 under index 2 in maxright just means there is a contigious array starting from the right end
        # with total sum equal 4
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
            # we should sum ove max N elements (the size of incoming array)
            # extract out the items outside of range
            # so, this is to keep the window of N elements max
            if j - deque[0] > N:
                deque.popleft()

            # P is an array of prefix sums, this allows us to find sum from deque[0] to j in O(1)
            ans = max(ans, P[j] - P[deque[0]])

            # There is no reason to keep items in the queue that are greater than P[j]
            # because when we do this ans = max(ans, P[j] - P[deque[0]]) it is useless calculation
            while deque and P[j] <= P[deque[-1]]:
                deque.pop()

            deque.append(j)

        return ans


if __name__ == '__main__':
    s = Solution2()
    s.maxSubarraySumCircular([1, -2, 3, -2])
    #s.maxSubarraySumCircular([5,-3,5])

