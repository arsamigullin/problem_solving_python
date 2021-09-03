from typing import List


class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        n = len(jobDifficulty)
        M = 10 ** 3 + 1
        memo = {}

        def dfs(i, d):
            if i >= n and d == 0:
                return 0
            if d == 0:
                return M
            if (i, d) not in memo:
                m = -1
                res = M
                for j in range(i, n):
                    m = max(jobDifficulty[j], m)
                    res = min(res, dfs(j + 1, d - 1) + m)

                memo[(i, d)] = res
            return memo[(i, d)]

        ans = dfs(0, d)
        print(memo)
        return ans

    # this is wrong
    def minDifficulty2(self, jobDifficulty: List[int], d: int) -> int:
        n = len(jobDifficulty)
        #jobDifficulty.sort(reverse=True)
        dp = [[10**10]*(n) for _ in range(d)]
        dp[0][0] = jobDifficulty[0]
        for i in range(1, n):
            #dp[0][i] = jobDifficulty[i]
            dp[0][i] = max(jobDifficulty[i],dp[0][i-1])
        # min(dp.get((i, j), math.inf), mx + dp[i-1, k-1])
        for day in range(1, d):
            m = -1
            for i in range(n):
                m = max(m, jobDifficulty[i])
                if i == 0:
                    dp[day][i] = m
                    #dp[day][i] = jobDifficulty[i] #min(dp[day - 1][i] + jobDifficulty[i], dp[day][i])
                else:
                    dp[day][i] = max(dp[day-1][i-1]+m, dp[day][i-1]+m)
            #dp[day][i] = max(dp[day][i], dp[day-1][i-1])

        print(dp[-1][-1])

    # working bottom-up
    def dp(slef, jobs, d):
        A = [[float("inf")] * d for i in range(len(jobs))]
        A[0][0] = jobs[0]
        for i in range(1, len(jobs)):
            A[i][0] = max(A[i - 1][0], jobs[i])

        for i in range(1, len(jobs)):
            for j in range(1, min(i + 1, d)):
                for k in range(i):
                    A[i][j] = min(A[i][j], A[k][j - 1] + max(jobs[k + 1:i + 1]))

        return A[-1][-1]

    import math
    def minDifficulty3(self, J, d):
        if len(J) < d: return -1
        n = len(J)
        dp = [[10**10]*n for _ in range(d)] # (index of day, index of the last finished job)
        dp[0][0] = J[0]
        for i in range(1,n):
            # the base case, all jobs need to be finish in one day
            dp[0][i] = max(dp[0][i-1], J[i])

        for day in range(1, d):
            for job_ind in range(day, n):
                mx = J[job_ind]
                for k in range(job_ind, -1, -1):
                    mx = max(mx, J[k])
                    dp[day][job_ind] = min(dp[day][job_ind], mx + dp[day - 1][k - 1])

        return dp[-1][-1]

if __name__ == '__main__':
    s = Solution()
    #s.minDifficulty2([6,5,4,3,2,1], 2)
    s.minDifficulty3([11,111,22,222,33,333,44,444],6)