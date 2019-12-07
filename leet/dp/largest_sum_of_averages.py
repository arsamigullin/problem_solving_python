def largestSumOfAverages(A, K):
    P = [0]
    # prefix sum technique
    # P contains sums of  of elements so the latest item contains sum of all elements
    for x in A:
        P.append(P[-1] + x)

    def average(i, j):
        return (P[j] - P[i]) / float(j - i)

    N = len(A)
    # initially dp contains averages from of P starting from 0 and ending to N
    # that is, (P[N] - P[0])/(N-0) and so on
    # as you can see it contains the averages of a groups with length greater that K
    dp = [average(i, N) for i in range(N)]
    for k in range(K - 1):
        print("K is:" + str(k))
        for i in range(N):
            for j in range(i + 1, N):
                print(f"i={i} dp[i]={dp[i]} j={j} dp[j]={dp[j]} average={average(i,j)} average+dp[j]={average(i, j) + dp[j]} j-i={j-i}")
                dp[i] = max(dp[i], average(i, j) + dp[j])

    return dp[0]

if __name__ == "__main__":
    largestSumOfAverages([9,1,2,3,9], 3)