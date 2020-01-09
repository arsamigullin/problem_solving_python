import math


class Solution:
    def divide(self, A, B):
        if (A == -2147483648 and B == -1): return 2147483647
        a, b, res = abs(A), abs(B), 0
        for x in range(32)[::-1]:
            if (a >> x) - b >= 0:
                res += 1 << x
                a -= b << x
        return res if (A > 0) == (B > 0) else -res

# from python help
# log(...)
#    log(x, [base=math.e])
#    Return the logarithm of x to the given base.
#    If the base not specified, returns the natural logarithm (base e) of x.
#   the solution comes from formula
#   e^ln(abs(A)/abs(B)) = e^(ln(abs(A)) - ln(abs(B)))

    def divide(self, A, B):
        if (A == -2147483648 and B == -1): return 2147483647
        if B == 0:
           return 0
        if B == 1:
            return A
        sign = 1 if A > 0 and B > 0 or A < 0 and B < 0 else -1
        res = int(math.exp(math.log(abs(A)) - math.log(abs(B))))
        return res if sign > 0 else -res


if __name__ == "__main__":
    s = Solution()
    s.divide(7, 3)
