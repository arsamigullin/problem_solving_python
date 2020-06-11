class Solution:
    def toLowerCase(self, str: str) -> str:
        s  = list(str)
        for i in range(len(s)):
            order = ord(s[i])
            if 65<=order<=90:
                s[i] = chr(order + 32)
        return ''.join(s)