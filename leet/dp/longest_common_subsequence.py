def solutionWithoutMem(a,b,n,m):
    if n == 0 or m == 0:
        return 0
    if a[n-1] == b[m-1]:
        return solutionWithoutMem(a, b, n-1, m-1) + 1
    return max(solutionWithoutMem(a, b, n, m-1), solutionWithoutMem(a, b, n-1, m))


def solutionMem(a,b,n,m,d):
    if n==0 or m==0:
        return 0
    key = str(n - 1) + "|" + str(m - 1)
    if key not in d:
        if (a[n-1] == b[m-1]):
            d[key] = solutionMem(a,b,n-1,m-1,d) + 1
        else:
            d[key]=max(solutionMem(a,b,n-1,m,d), solutionMem(a,b,n,m-1,d))
    return d[key]

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if len(text1) < len(text2):
            text1, text2 = text2, text1
        l1, l2 = len(text1), len(text2)
        curr = [0] * (l2 + 1)
        prev = [0] * (l2 + 1)
        for i in range(l1):
            for j in range(l2):
                if text1[i] == text2[j]:
                    curr[j+1] = prev[j] + 1
                else:
                    if curr[j] > prev[j+1]:
                        curr[j+1] = curr[j]
                    else:
                        curr[j+1] = prev[j+1]
            curr, prev = prev, curr
        return prev[-1]

if __name__ == "__main__":
    a="ylqpejqbalahwr"
    b="yrkzavgdmdgtqpg"
    s = Solution()
    s.longestCommonSubsequence(a,b)
    d = dict()
    print(solutionMem(a, b, len(a), len(b), d))
    print("dfs")
    #print (solution(a, b, len(a), len(b)))