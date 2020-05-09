class Solution:
    '''
    bit shift idea
    let's consider numbers
    [2,79822]
    10011011111001110
    00000000000000010
    The answer is 0
    We shift both strings to the right
    After two sifts number 2 becomes 0
    we do shifts until numbers are equal
    '''

    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        shift = 0
        while m < n:
            m = m >> 1
            n = n >> 1
            shift+=1
        # must to put m back
        return m<<shift

# Brian Kernighan's Algorithm
class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        while m < n:
            n = n&(n-1)
        return m&n
