# this solution is much shorter than the one below
# Observation:
# We compare the latest item in stack with
# if the latest element in stack is greater than current element x
# monotonous stack technique
# Algo:
# 1. Once we found that the top element in stack is greater than current element (x) this means
# the current element is the nearest minimum to the right from the top element of stack
# 2. We pop it to figure out the distance between the top element in stack and the current element x
# The trick is that in stack the very left neighbor of top element is its nearest minimum to the left
# 3. Since we have while we do the same to the next top element in stack. The same item can be the nearest
# minimum element for the several items
# Let's consider array [3,1,2,4]. We add 0 at the beginning and at the end [0,3,1,2,4,0]
# stack is empty, stack = [0]
# 0 is not > 3, stack = [0, 3]
# 3 is > 1, pop 3, find distance between 0 and 3, and 3 and 1, stack = [0]
# (in while) 0 is not > 1, stack = [0,1]
# 1 is not > 2, stack = [0,1,2]
# 2 is not > 4, stack = [0,1,2,4]
# 4 is > 0, pop 4, find distance between 2 and 4, and 4 and 0, stack = [0,1,2]
# (in while) 2 is > 0, pop 2, find distance between 1 and 2, and 2 and 0, stack = [0,1]
# (in while) 1 is > 0, pop 1, find distance between 0 and 1, and 1 and 0, stack = [0,0]

# the key points here
# j is the middle item of two arrays
# One array is of i-j length
# another array is of j-k length
# the length of the subbarray is also the nuber
class Solution1:
    def sumSubarrayMins(self, A):
        res = 0
        s = []
        A = [0] + A + [0]
        for i, x in enumerate(A):
            while s and A[s[-1]] > x:
                j = s.pop()
                k = s[-1]
                res += A[j] * (i - j) * (j - k)
            s.append(i)
        return res % (10**9 + 7)


class Solution(object):
    def sumSubarrayMins(self, A):
        MOD = 10**9 + 7
        N = len(A)
        # for each item we find the nearest minimum item to the left
        # prev has i* - 1 in increasing order of A[i* - 1]
        # where i* is the answer to query j
        stack = []
        prev = [None] * N
        for i in range(N):
            while stack and A[i] <= A[stack[-1]]:
                stack.pop()
            prev[i] = stack[-1] if stack else -1
            stack.append(i)

        # Also for each item we find the nearest minimum item to the right
        # next has k* + 1 in increasing order of A[k* + 1]
        # where k* is the answer to query j
        stack = []
        next_ = [None] * N
        for k in range(N-1, -1, -1):
            while stack and A[k] < A[stack[-1]]:
                stack.pop()
            next_[k] = stack[-1] if stack else N
            stack.append(k)

        # Use prev/next array to count answer
        # For each item we have the distance to minimum elements to the left and to the right
        # the formula is the following: distance_left * distance_right * current_element
        return sum((i - prev[i]) * (next_[i] - i) * A[i]
                   for i in range(N)) % MOD

if __name__ == "__main__":
    s = Solution1()
    s.sumSubarrayMins([11,1,1,2,3,1])
    s.sumSubarrayMins([3,1,2,4])
    s.sumSubarrayMins([10, 3, 4, 5, 3, 2, 3, 10])