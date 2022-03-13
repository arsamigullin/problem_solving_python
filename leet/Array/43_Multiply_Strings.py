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

# the most correct one
class Solution5:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"
        n = len(num1)
        m = len(num2)
        ans = [0] * (n + m) # this is collecting num in reversed order
        for p, dig1 in enumerate(num1[::-1]):
            dig1 = ord(dig1) - ord('0')
            for q, dig2 in enumerate(num2[::-1]):
                i = p + q
                carry = ans[i]
                dig2 = ord(dig2) - ord('0')
                mul = dig1 * dig2 + carry
                ans[i] = mul % 10
                ans[i + 1] += mul // 10

        # that is why we have to get rid of the zeros (otherwise, after reversing they are going to be the leading zeros)
        while ans[-1] == 0:
            ans.pop()
        return ''.join(str(dig) for dig in reversed(ans))

if __name__ == '__main__':
    s = Solution5()
    s.multiply("9","9")
    s.multiply("123", "456")