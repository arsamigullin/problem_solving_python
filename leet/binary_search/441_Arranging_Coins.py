
# we want to construct staircase shape

# Brute force
class Solution:
    def arrangeCoins(self, n: int) -> int:
        i = 1
        while n - i > 0:
            n -= i
            i += 1

        return (i - 1) + (n - i == 0)

class Solution:
    def arrangeCoins(self, n: int) -> int:

        lo = 1
        hi = n + 1
        while lo <= hi:
            k = lo + (hi - lo) // 2
            # this is coins used at rows from 1 to k
            used_in_k_rows = k * (k + 1) // 2
            # if coins used from 1 to k rows are equal n
            if used_in_k_rows == n:
                return k
            if used_in_k_rows <= n:
                lo = k + 1
            else:
                hi = k - 1
        return hi

#If we look deeper into the formula of the problem, we could actually solve it with the help of mathematics, without using any iteration.
#As a reminder, the constraint of the problem can be expressed as follows:
# k(1+k)/2 <= N
class Solution:
    def arrangeCoins(self, n: int) -> int:
        return (int)((2 * n + 0.25)**0.5 - 0.5)