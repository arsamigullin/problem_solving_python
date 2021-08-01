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