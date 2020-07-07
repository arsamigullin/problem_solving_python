import math


# Note, we need to get exact n 'A'
class SolutionMy:
    def minSteps(self, n: int) -> int:
        # method to print the divisors
        if n == 1:
            return 0

        # that is why we need to find divisors
        # for example, n = 6. 4 is not divisor of 6 so, there is no way to get 6 'A' from 4 'A'
        # but 3 is divisor of 6. So, we can get 6 'A' having 'AAA'
        def divisors(n):
            divs = [1]
            for i in range(2, int(math.sqrt(n)) + 1):
                if n % i == 0:
                    divs.append(i)
                    divs.append(n // i)
            # divs.append(n)
            return list(set(divs))

        divs = divisors(n)
        print(divs)
        dp = [n] * (n + 1)
        dp[0] = 0
        for i in range(1, n + 1):
            # iterating over divisor
            for d in divs:
                if d == 1:
                    # In this case we need to use i 'A'
                    dp[i] = min(dp[i], i)
                elif i % d == 0:
                    dp[i] = min(dp[i], d + dp[i // d])
        return dp[-1]


class Solution:
    def minSteps(self, n: int) -> int:
        d = 2
        ans = 0
        while n > 1:
            while n % d == 0:
                n //= d
                ans += d
            d += 1
        return ans
