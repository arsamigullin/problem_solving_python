import math

# this is really similar to coin change problem
class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        square_nums = [i ** 2 for i in range(0, int(math.sqrt(n)) + 1)]

        dp = [float('inf')] * (n + 1)
        # bottom case
        dp[0] = 0

        for i in range(1, n + 1):
            for square in square_nums:
                if i < square:
                    break
                dp[i] = min(dp[i], dp[i - square] + 1)

        return dp[-1]


class Solution:
    def numSquares(self, n):

        # list of square numbers that are less than `n`
        square_nums = [i * i for i in range(1, int(n ** 0.5) + 1)]

        level = 0
        queue = {n}
        while queue:
            level += 1
            # ! Important: use set() instead of list() to eliminate the redundancy,
            # which would even provide a 5-times speedup, 200ms vs. 1000ms.
            next_queue = set()
            # construct the queue for the next level
            for remainder in queue:
                for square_num in square_nums:
                    if remainder == square_num:
                        return level  # find the node!
                    elif remainder < square_num:
                        break
                    else:
                        next_queue.add(remainder - square_num)
            queue = next_queue
        return level

from math import sqrt
# Logic: Use Lagrange's 4-square theorem
class Solution:
    def numSquares(self, n: int) -> int:
        # Reduction by factor of 4
        while (n % 4 == 0):
            n //= 4

        # Quick response for n = 8k + 7
        if n % 8 == 7:
            return 4

        # Check whether n = a^2 + b^2
        for a in range(int(sqrt(n)) + 1):
            b = int(sqrt(n - a * a))
            if (a ** 2 + b ** 2) == n:
                return (a > 0) + (b > 0)

        # n = a^2 + b^2 + c^2
        return 3