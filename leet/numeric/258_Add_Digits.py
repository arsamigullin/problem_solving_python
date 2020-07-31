
# this is digital root problem

class Solution1:
    '''
    the formula of digital root is
    dr = 1 + (n-1) mod 9
    source https://mathworld.wolfram.com/DigitalRoot.html
    '''
    def addDigits(self, num: int) -> int:
        return 0 if num == 0 else 1 + (num - 1) % 9

# another option
class Solution:
    def addDigits(self, num: int) -> int:
        while num > 9:
            m = 0
            while num:
                num, tmp = divmod(num, 10)
                m += tmp
            num = m
        return num


C1.X 1
C1.Y 2
C2.X 1
C2.Y 2
A.X 2
A.Y 4
B.X 2
B.Y 2
