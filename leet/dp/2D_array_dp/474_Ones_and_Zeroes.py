from typing import List


class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        dp = [[0]*(n+1) for _ in range(m+1)]
        for i in range(len(strs)):
            zeros = strs[i].count('0')
            ones = strs[i].count('1')
            # since we are limited by m and n
            # we start a loop from m and n and do backward
            # if zeros or ones are greater m or n
            # the loop never will start
            for i in range(m,zeros-1,-1):
                for j in range(n,ones-1,-1):
                    print(f"dp[{i}][{j}] = dp[{i-zeros}][{j-ones}]+1")
                    dp[i][j] = max(1+dp[i-zeros][j-ones], dp[i][j])
        print(dp)
        return dp[m][n]


if __name__ == '__main__':
    s = Solution()
    s.findMaxForm(["10","0001","111001","1","0"],5,3)
