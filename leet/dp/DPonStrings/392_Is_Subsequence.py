# similar
#1143. Longest Common Subsequence

# brute force
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        n = len(s)
        m = len(t)

        k = 0
        num = 0
        for i in range(n):
            for j in range(k, m):
                if s[i] == t[j]:
                    k = j + 1
                    num+=1
                    break
        return num == n

# two pointers
# O(m)
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        n = len(s)
        m = len(t)
        i = j = 0
        while i < n and j < m:
            if s[i] == t[j]:
                i += 1
            j += 1

        return i == n

# recursive dp
# O(nxm)
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        memo = {}
        def helper(i, j):
            if i >= len(s):
                return True
            if j >= len(t):
                return False
            if (i,j) not in memo:
                if s[i] == t[j]:
                    memo[(i,j)] = helper(i+1, j+1)
                else:
                    memo[(i,j)] = helper(i, j+1)
            return memo[(i,j)]

        return helper(0,0)