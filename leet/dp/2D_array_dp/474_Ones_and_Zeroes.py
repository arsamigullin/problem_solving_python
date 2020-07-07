from typing import List


class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        dp = [[0]*(n+1) for _ in range(m+1)]
        for i in range(len(strs)):
            ze = strs[i].count('0')
            on = strs[i].count('1')
            for i in range(m,ze-1,-1):
                for j in range(n,on-1,-1):
                    dp[i][j] = max(1+dp[i-ze][j-on], dp[i][j])
        print(dp)
        return dp[m][n]


if __name__ == '__main__':
    s = Solution()
    s.findMaxForm(["10","0001","111001","1","0"],5,3)
