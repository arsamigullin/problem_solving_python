from functools import reduce


class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        s=0
        m=1
        while n>=10:
            r=n%10
            s+=r
            m*=r
            n=n//10
        return (m*n) - (s+n)


class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        z = [int(i) for i in str(n)]
        return reduce(lambda x, y: x*y, z, 1)-reduce(lambda x, y: x+y, z, 0)