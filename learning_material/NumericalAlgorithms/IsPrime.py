import random


class Solution:
    def is_prime(self, p, tests_num):
        seq = range(1, p)
        for _ in range(tests_num):
            n = random.choice(seq)
            if (n ** (p - 1)) % p != 1:
                return False
        return True