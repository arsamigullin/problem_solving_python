class Solution1:
    def countBinarySubstrings(self, s: str) -> int:
        left_cnt = -1
        res = 0
        k = 0
        while k < len(s):
            j = k + 1
            while j < len(s) and s[j - 1] == s[j]:
                j += 1
            if left_cnt >= 0:
                res += min(left_cnt, j - k)
            left_cnt = j - k
            k = j
        return res


class Solution(object):
    def countBinarySubstrings(self, s):
        ans, prev, cur = 0, 0, 1
        for i in range(1, len(s)):
            if s[i - 1] != s[i]:
                ans += min(prev, cur)
                prev, cur = cur, 1
            else:
                cur += 1

        return ans + min(prev, cur)