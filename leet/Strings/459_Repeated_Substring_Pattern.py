class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        i, j = 0, 1
        if len(s) == 1:
            return False
        if len(set(s)) == 1:
            return True
        if len(s) % 2 == 1:
            return False
        n = len(s)
        maxi = 0
        while j < n:
            if s[i] == s[j]:
                i += 1
                j += 1
            else:
                if i == 0:
                    j = max(maxi + 1, j+1)
                else:
                    j = maxi + 1
                i = 0
            maxi = max(maxi, i)

        return i >= n // 2 + n % 2

if __name__ == '__main__':
    s = Solution()
    s.repeatedSubstringPattern("abaababaab")