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


if __name__ == "__main__":
    a="ylqpejqbalahwr"
    b="yrkzavgdmdgtqpg"
    d = dict()
    print(solutionMem(a, b, len(a), len(b), d))
    print("dfs")
    #print (solution(a, b, len(a), len(b)))