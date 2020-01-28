# Brute
# local inversion is also global inversion with j- i = 1
# but global inversion with j-i>1 is not a local inversion
# that is why we want to determine if all x are less that A[j] with j-i >1
class Solution(object):
    def isIdealPermutation(self, A):
        return all(x < A[j]
                   for i, x in enumerate(A)
                   for j in range(i+2, len(A)))


#In performing a brute force, we repeatedly want to check whether there is some j >= i+2 for which A[i] > A[j].
#This is the same as checking for A[i] > min(A[i+2:]). If we knew these minimums min(A[0:]), min(A[1:]), min(A[2:]), ...
#we could make this check quickly.
class Solution(object):
    def isIdealPermutation(self, A):
        N = len(A)
        floor = N
        for i in range(N-1, -1, -1):
            floor = min(floor, A[i])
            if i >= 2 and A[i-2] > floor:
                return False
        return True


#Let's try to characterize all ideal permutations: ones that do not have non-local inversions. Where does the 0 go?
#If the 0 occurs at index 2 or greater, then A[0] > A[2] = 0 is a non-local inversion.
# So 0 can only occur at index 0 or 1. If A[1] = 0,
# then we must have A[0] = 1 otherwise A[0] > A[j] = 1 is a non-local inversion.
# Otherwise, A[0] = 0.
# To recap, the possibilities are either A = [0] + (ideal permutation of 1...N-1) or A = [1, 0] + (ideal permutation of 2...N-1)

class Solution(object):
    def isIdealPermutation(self, A):
        return all(abs(i-x) <= 1 for i,x in enumerate(A))