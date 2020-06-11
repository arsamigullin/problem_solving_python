class Solution:
    def maxSumAfterPartitioning(self, A, K: int) -> int:
        n = len(A)
        dp = [0] * (n +1)
        i = 1
        while i<n+1:
            loc_max = float('-inf')
            j = 1
            # here we update dp[i]
            while j < min(i,K)+1:
                loc_max = max(loc_max, A[i-j])
                # by i-j we are taking the sum of previous calculated maxsum and
                # and by loc_max*j we compensating this subtraction
                dp[i] = max(dp[i], dp[i-j] + loc_max*j)
                j+=1
            i+=1
        return dp[n]
if __name__ == "__main__":
    s = Solution()
    s.maxSumAfterPartitioning([1,15,7,9,2,5,10], 3)