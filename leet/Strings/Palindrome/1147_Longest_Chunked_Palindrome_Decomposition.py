import random
class Solution1:
    def longestDecomposition(self, text: str) -> int:
        n = len(text)
        i = 0
        j = n - 1
        cnt = 0
        while i <= j:
            leftCh = text[i]
            right = j
            while i <= j:
                if i == j:
                    cnt += 1
                elif text[j] == leftCh:
                    dist = right - j + 1
                    if text[j:j + dist] == text[i:i + dist]:
                        cnt += 2
                        i += dist
                        j -= 1
                        break
                j -= 1
        return cnt


class Solution:
    def longestDecomposition(self, S):
        res, l, r = 0, "", ""
        for i, j in zip(S, S[::-1]):
            l, r = l + i, j + r
            if l == r:
                res, l, r = res + 1, "", ""
        return res

if __name__ == '__main__':
    s = Solution()
    s.longestDecomposition("ghiabcdefhelloadamhelloabcdefghi")