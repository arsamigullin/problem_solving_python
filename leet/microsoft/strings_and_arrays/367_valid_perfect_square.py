# binary search
# master theorem
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        i = 1
        while(i * i<= num):

            # If (i * i = n)
            if (num / i == i):
                return True

            i = i + 1
        return False

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num < 2:
            return True
        hi = num//2
        lo = 2
        while lo<=hi:
            guess = lo + (hi-lo)//2
            sq = guess**2
            if sq == num:
                return True
            elif sq > num:
                hi = guess - 1
            else:
                lo = guess + 1
        return False

#  Newton's Method
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num < 2:
            return True

        x = num // 2
        while x * x > num:
            x = (x + num // x) // 2
        return x * x == num

if __name__ == '__main__':
    s = Solution()
    s.isPerfectSquare(9)