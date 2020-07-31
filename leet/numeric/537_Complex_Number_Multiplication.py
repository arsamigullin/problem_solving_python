import re


class Solution:
    def complexNumberMultiply(self, a: str, b: str) -> str:
        #a = "4+2i"
        # the result is ['4','2','']
        num1 = re.split('\\+|i', a)
        num2 = re.split('\\+|i', b)

        # extract real and imaginary parts

        re1, imag1 = int(num1[0]), int(num1[1])
        re2, imag2 = int(num2[0]), int(num2[1])

        # and multiply them
        return f"{(re1 * re2 - imag1 * imag2)}+{(re1 * imag2 + re2 * imag1)}i"
