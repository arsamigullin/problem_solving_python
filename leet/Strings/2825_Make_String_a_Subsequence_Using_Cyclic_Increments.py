class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        n = len(str1)
        m = len(str2)
        i, j = 0, 0

        def get_next_char(ch):
            o = ord('a') + (ord(ch) - ord('a') + 1) % 26
            return chr(o)

        while i < n and j < m:
            if str1[i] == str2[j] or get_next_char(str1[i]) == str2[j]:
                j += 1
            i += 1

        return j >= m
