class Solution:
    def isPowerOfThree(self, n):
        return 0 if n <= 0 else 1162261467 % n == 0


def isPowerOfThree(self, n: int) -> bool:
    # Assuming I won't be calling this function once
    # Hence I can go ahead and save the max power of 3
    # allowed. Just a way of countering how this solution is better
    maxPower = 3 ** (int(math.log(2 ** 31 - 1, 3)))

    return n > 0 and maxPower % n == 0

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        while n >1.0:
            n = n/3
        return n == 1


from math import log
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        """
        :type n: int
        :rtype: bool
        """
        # Since error exist, can't use float.is_integer() to check
        # So I choose to check it back
        if n <= 0: return False
        res = round(log(n, 3))
        return 3**res == n