import string


class Solution:
    def titleToNumber(self, s: str) -> int:
        d = {letter: i + 1 for i, letter in enumerate(string.ascii_uppercase)}
        letter_count = 26
        count = len(s)
        res = 0
        # 423 the base is 10
        # to get 400 we do 4 * 10 * 10
        # to get 20 we do 2 * 10
        # to get 3 we do 3


        # the same is here
        # ZYA
        # x is a place holder for "0"
        # to  get Zxx we do Z(26) * 26 * 26
        # to get Yx we do Y(25) * 26
        # to get A  we do A(1)
        for i in range(count):
            res += d[s[i]] * letter_count ** (count - i - 1)

        return res


