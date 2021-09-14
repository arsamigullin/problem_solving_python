import bisect

# the same as below
import math

# the same as the right below solution
class Solution1:
    def minWindow(self, T: str, P: str) -> str:
        n = len(T)
        m = len(P)
        memo = {}
        # state here is i and j, the position in T where we've found the char under P[j]
        # meaning, if we search for P[j] in T starting from index i, then in memo we saving
        # found last index (ind) under (i,j), i.e. memo[(i,j)] = ind
        # ind is the index in T where the last char of P found
        #  (think of it as flatten tree where ind is root and (i,j) are children)
        # So let's say we have T = "abbcdebdde" and P = "bde"
        # the memo will look like this
        # {(5, 3): 6, (4, 2): 6, (2, 1): 6, (3, 1): 6, (7, 1): inf}
        def helper(i, j):
            if j >= m:
                return i
            if (i, j) not in memo:
                ind = T.find(P[j], i)
                memo[(i, j)] = math.inf if ind == -1 else helper(ind + 1, j + 1)
            return memo[(i, j)]

        length = n + 1
        result = ""
        for start in range(n):
            if T[start] == P[0]:
                end = helper(start + 1, 1)
                if end - start < length:
                    result = T[start: end]
                    length = end - start
        return result

if __name__ == '__main__':
    s = Solution1()
    s.minWindow("abbcdebdde","bde")

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
    def minWindow(self, T: str, P: str) -> str:
        start = -1
        ret = ""
        while True:
            first = start + 1
            for c in P:
                start = T.find(c, start + 1)
                if start == -1:
                    return ret
            start = end = start + 1
            for c in reversed(P):
                start = T.rfind(c, first, start)
            if not ret or len(ret) > end - start:
                ret = T[start:end]


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