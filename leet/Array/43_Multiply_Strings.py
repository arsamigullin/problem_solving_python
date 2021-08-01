class Solution:
    def multiply(self, A: str, B: str) -> str:
        result = 0
        for b in B:
            result *= 10
            b = ord(b) - ord('0')
            toAdd = 0
            carry = 0
            base = 1
            for i in range(len(A))[::-1]:
                a = b * (ord(A[i]) - ord('0')) + carry
                toAdd += (a % 10) * base
                carry = a // 10
                base *= 10
            result += toAdd + carry * base
        return str(result)

class SolutionMy:
    def multiply(self, A: str, B: str) -> str:

        tot = 0
        for i in range(len(B))[::-1]:
            b = ord(B[i]) - ord('0')
            carry = 0
            base = 1
            res=0
            for j in range(len(A))[::-1]:
                mul = b * (ord(A[j]) - ord('0'))
                carry, ans = divmod(mul+carry, 10)
                res += ans * base
                base*=10
            tot+=(res+carry*base)*10**(len(B)-1-i)
        return tot


class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """

        def convert_to_num(num):
            power = len(num) - 1
            res = 0
            for n in num:
                res += (10 ** power) * int(n)
                power -= 1
            return res

        return str(convert_to_num(num1) * convert_to_num(num2))

if __name__ == '__main__':
    s = Solution()
    s.multiply("123", "456")