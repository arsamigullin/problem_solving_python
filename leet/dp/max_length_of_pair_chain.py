# incorrect
import collections
def longestArithSeqLength(A):
    n = len(A)
    dp1 = [collections.defaultdict(int) for _ in range(n)]
    dp2 = [collections.defaultdict(int) for _ in range(n)]
    res = 0
    for i in range(1, n):
        for j in range(0, i):
            if A[i][0] <= A[j][1]:
                if A[j][0] > A[i][1]:
                    dp2[i][A[i][1]] = dp2[j][A[j][1]] + 1
                    res = max(res, dp2[i][A[i][1]])
            #elif A[i][0] == A[j][1]:
                #continue
            else:
                dp1[i][A[i][1]] = dp1[j][A[j][1]] + 1
                res = max(res, dp1[i][A[i][1]])

    return res + 1

# incorrect
import collections
def longestArithSeqLength1(A):
    n = len(A)
    dp = [collections.defaultdict(int) for _ in range(n)]
    res = 0
    for i in range(1, n):
        for j in range(0, i):
            if A[i][0] <= A[j][1]:
                if A[j][0] > A[i][1]:
                    dp[j][A[j][0]] = dp[i][A[i][1]] + 1
                    res = max(res, dp[j][A[j][0]])
            #elif A[i][0] == A[j][1]:
                #continue
            else:
                dp[i][A[i][1]] = dp[j][A[j][1]] + 1
                res = max(res, dp[i][A[i][1]])

    return res + 1

# correct but we have to sort by the second element of subarray, i.e. operator.itemgetter(1)
def findLongestChain(pairs):
    cur, ans = float('-inf'), 0
    for x, y in sorted(pairs, key = operator.itemgetter(1)):
        if cur < x:
            cur = y
            ans += 1
    return ans

# correct
def findLongestChain(self, pairs):
    pairs.sort()
    dp = [1] * len(pairs)

    for j in xrange(len(pairs)):
        for i in xrange(j):
            if pairs[i][1] < pairs[j][0]:
                dp[j] = max(dp[j], dp[i] + 1)

    return max(dp)

if __name__ == "__main__":
    #print(longestArithSeqLength([[3,4],[2,3],[1,2]]))
    #print(longestArithSeqLength([[1,2],[3,4],[4,5],[5,6]]))
    #print(longestArithSeqLength([[1, 2], [2, 3], [3, 4]]))
    #print(longestArithSeqLength([[-10, -8], [8, 9], [-5, 0], [6, 10], [-6, -4], [1, 7], [9, 10], [-4, 7]]))
    print(findLongestChain([[-9, -3], [-9, 1], [-7, -6], [-5, -4], [0, 3], [4, 5], [6, 10], [9, 10], [9, 10]]))