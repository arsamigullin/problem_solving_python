import string


class Solution:
    def convertToTitle(self, columnNumber: int) -> str:

        cols = {1 + i: letter for i, letter in enumerate(string.ascii_uppercase)}
        cols[0] = 'Z'
        res = []
        while columnNumber > 0:
            div, mod = divmod(columnNumber, 26)
            res.append(cols[mod])
            columnNumber //= 26
            if mod == 0:
                columnNumber -= 1
        res.reverse()
        return ''.join(res)


class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        cols = {i: letter for i, letter in enumerate(string.ascii_uppercase)}
        res = []
        while columnNumber > 0:
            columnNumber -= 1
            div, mod = divmod(columnNumber, 26)
            res.append(cols[mod])
            columnNumber //= 26
        res.reverse()
        return ''.join(res)


class Solution:
    def convertToTitle(self, n):
        r = ''
        while(n>0):
            n -= 1
            r = chr(n%26+65) + r
            n /= 26
        return r