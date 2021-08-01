import bisect
class Solution:
    def minWindow(self, T: str, P: str) -> str:
        def dfs(i, j):
            if j == len(P): return i
            print(i,j)
            if (i, j) not in memo:
                ind = T.find(P[j], i + 1)
                memo[(i, j)] = float('inf') if ind == -1 else dfs(ind, j + 1)
            return memo[(i, j)]

        l, res, memo = float('inf'), '', {}
        for i, s in enumerate(T):
            if s == P[0]:
                j = dfs(i, 1)
                if j - i < l:
                    l, res = j - i, T[i:j + 1]
        return res


class Solution1:
    def minWindow(self, s1: str, s2: str) -> str:
        start = -1
        ret = ""
        while True:
            first = start + 1
            for c in s2:
                start = s1.find(c, start+1)
                if start == -1:
                    return ret
            start = end = start + 1
            for c in reversed(s2):
                start = s1.rfind(c, first, start)
            if not ret or len(ret) > end - start:
                ret = s1[start:end]


# preprocessing needs to collect indices of the P we will return in case of mistmatch
# if P is sevsevsev, after preprocessing it returns [-1,0,0,0,1,2,3,4,5,6]
def KMP_preprocessing(text, pattern):
    m = len(pattern)
    i, j = 0, -1
    s = [0] * (m + 1)
    s[0] = -1
    while i < m:
        # once mismatch found, reset j to s[j]
        # s[j] stores the previous index of the char under pattern[j]
        # for exmaple, P is sesekl then s is [-1,0,0,1,2,0,0]
        # s[4] stores the index which is 2 of the previous e char
        while j >= 0 and pattern[j] != pattern[i]:
            j = s[j]
        i += 1
        j += 1
        s[i] = j
    return s


def KMP_search(text, pattern):
    dp = KMP_preprocessing(text, pattern)

    n = len(text)
    m = len(pattern)
    freq = 0
    i, j = 0, 0
    res = []
    while i < n:
        # once there is a mismatch
        # s[j] stores the previous index of the char under pattern[j]
        # so it moves the j pointer to the nearest previous pattern[j] match
        while j >= 0 and text[i] != pattern[j]:
            j = dp[j]
        i += 1
        j += 1
        if j == m:
            # NOTE: to find the first occurence index must use i-m
            res.append(i - m)
            freq += 1
            j = dp[j]

    print(res)
    return freq

if __name__ == '__main__':

    T = "fffffffsssa"
    P = "ffsa"
    s = Solution()
    s.minWindow(T, P)
    #KMP_search(T ,P)