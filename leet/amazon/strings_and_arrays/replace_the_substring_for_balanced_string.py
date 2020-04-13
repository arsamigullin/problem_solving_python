import collections
class Solution:
    def balancedString(self, s: str) -> int:
        n, buf = len(s) // 4, {'Q': 0, 'W': 0, 'E': 0, 'R': 0}
        for x in s: buf[x] += 1
        wait = len([ k for k,v in buf.items() if n < v ])
        if not wait: return 0
        best, i = n * 4, 0
        for j, x in enumerate(s):
            buf[x] -= 1
            if buf[x] == n:
                wait -= 1
            if wait:
                continue
            while buf[s[i]] < n:
                buf[s[i]] += 1
                i += 1
            best = min(j - i + 1, best)
        return best


class Solution:
    def balancedString(self, s: str) -> int:
        n = len(s)
        cnt = {k: v - n // 4 for k, v in collections.Counter(s).items() if v > n // 4}
        if not cnt: return 0
        i, ans = 0, n
        for j in range(n):
            if s[j] in cnt:
                cnt[s[j]] -= 1
            while all(v <= 0 for v in cnt.values()):
                ans = min(ans, j - i + 1)  # s[i:j+1] covers all exceeding letters
                if s[i] in cnt:
                    cnt[s[i]] += 1
                i += 1  # move i to the right to be more concise

        return ans


if __name__ == "__main__":
    s = Solution()
    s.balancedString("WQWRQQQW")
    s.balancedString("WWEQERQWQWWRWWERQWEQ")

