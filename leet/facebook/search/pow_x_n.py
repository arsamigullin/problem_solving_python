# Algo
# if the power (n) is less than 0 we should make n greater that 0 by dividing 1 to x because
# x^-1 is 1/x. So, for example x = 2, n = -3, the x will be 1/2 and then n is 3

class PowSolution:
    def myPow(self, x: float, n: int) -> float:
        if n<0:
            x = 1/x
            n=-n
        def find(num, power):
            if power == 0:
                return 1
            half = find(num, power//2)
            if power%2==0:
                return half * half
            else:
                return half * half * x
        return find(x, n)


class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n<0:
            x = 1/x
            n=-n
        ans = 1
        current_prod = x
        i = n
        while i>0:
            if i%2 == 1:
                ans *= current_prod
            current_prod*=current_prod
            i//=2
        return ans

if __name__ == "__main__":
    s = PowSolution()
    s.myPow(2,6)
    s= Solution()
    s.myPow(2,6)