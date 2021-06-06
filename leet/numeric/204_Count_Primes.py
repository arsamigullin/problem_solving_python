from math import ceil


class Solution:
    def countPrimes(self, n):
        # we mark with 1 all numbers to be prime
        sieve = [1] * (n+1)
        # except 0 and 1
        sieve[0] = 0
        sieve[1] = 0
        # we reduce the steps to the sqrt
        for k in range(ceil(n ** 0.5) + 1):
            # if the number is marked as prime
            if sieve[k]:
                # starting from k*k till n+1 with step k
                for i in range(k * k, n + 1, k):
                    # we un-mark this number
                    sieve[i] = 0

        return sum(sieve[:-1])


if __name__ == '__main__':
    s = Solution()
    s.countPrimes(100)