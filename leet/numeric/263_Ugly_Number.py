import math
import random

# Theorem 31.8 (Unique factorization) Cormen
# There is exactly one way to write any composite integer a as a product of the form
# As an example, the number 6000 is uniquely factored into primes as 2**4, 3, 5**3
class Solution:
    def isUgly(self, num: int) -> bool:
        if num < 1:
            return False
        primes = [2, 3, 5]
        while any(num % i == 0 for i in primes):
            for i in primes:
                if num % i == 0:
                    num /= i

        return num == 1




class SolutionWrong:
    def isUgly(self, num: int) -> bool:

        val = int(math.sqrt(abs(num))) + 1
        prime_factors = {2, 3, 5}
        def is_prime(p, tests_num):
            seq = range(1, p)
            for _ in range(tests_num):
                n = random.choice(seq)
                if (n ** (p - 1)) % p != 1:
                    return False
            return True

        for i in range(2, val):
            if num % i == 0:
                opposite = abs(num // i)
                if i > 1 and is_prime(i, 10) and i not in prime_factors:
                    return False
                if opposite > 1 and is_prime(opposite, 10) and opposite not in prime_factors:
                    return False
        return True


if __name__ == '__main__':
    s = Solution()
    s.isUgly(-2147483648)