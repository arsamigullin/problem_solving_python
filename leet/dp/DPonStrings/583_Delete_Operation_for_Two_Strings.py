
class SolutionMy:
    def minDistance(self, word1: str, word2: str) -> int:
        n = len(word1)
        m = len(word2)
        d = {}
        def helper(i, j):
            if (i,j) in d:
                return d[(i,j)]
            if i >=n:
                return m-j
            if j >=m:
                return n-i

            if word1[i] == word2[j]:
                d[(i,j)]=helper(i+1, j+1)
            else:
                d[(i,j)]= min(helper(i+1,j), helper(i,j+1)) + 1
            return d[(i,j)]
        return helper(0,0)


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        l1,l2 = len(word1),len(word2)
        if not word1 or not word1: return max(l1,l2)
        dp = [ i for i in range(l2+1) ]
        for i in range(l1):
            p = i+1
            for j in range(l2):
                dp[j],p = p,dp[j] if word1[i]==word2[j] else min(p,dp[j+1])+1
            dp[-1]=p
        return dp[-1]


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = [x for x in range(len(word2)+1)]
        for i in range(len(word1)):
            newdp = dp[:]
            newdp[0] = (i+1)
            for j in range(len(word2)):
                if word1[i]==word2[j]:
                    newdp[j+1] = dp[j]
                else:
                    newdp[j+1] = 1+min(dp[j+1], newdp[j])
            dp = newdp
        return dp[-1]