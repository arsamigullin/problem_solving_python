class Solution:
    def isArmstrong(self, n: int) -> bool:
        num_str = str(n)
        power = len(num_str)
        result = 0
        for ch in num_str:
            result +=int(ch)**power
        return result == n


import math


class Solution:
    def isArmstrong(self, n: int) -> bool:
        power = int(math.log(n, 10)) + 1
        result = 0
        init = n
        while n != 0:
            num = n % 10
            result += num ** power
            n //= 10
        return result == init
