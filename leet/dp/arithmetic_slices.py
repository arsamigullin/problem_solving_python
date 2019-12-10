
#wrong solution
def solution(arr):
    n = len(arr)
    d = dict()

    def find_slice(i, diff):
        if i >= n:
            return 0
        total = 0
        while i + 1 < n:
            key = str(i) + "|" + str(i + 1)
            if key not in d:
                if arr[i + 1] - arr[i] == diff:
                    d[key] = find_slice(i + 1, diff, ) + 1
                    total += d[key]
            else:
                total += d[key]
            i += 1

        return total

    return find_slice(1, arr[1] - arr[0])

#wrong solution
def solution2(arr):
    n = len(arr)
    def find_slice(i, diff):
        if i >= n:
            return 0
        total = 0
        while i + 1 < n:
            if arr[i + 1] - arr[i] == diff:
                total += find_slice(i + 1, diff, ) + 1
            i += 1

        return total

    return find_slice(1, arr[1] - arr[0])

#correct solution
def solution3(arr):

    if len(arr) <=3:
        return 0
    diff = arr[1] - arr[0]
    count = 0
    add_to_cnt = 1
    for i in range(1, len(arr)-1):
        if arr[i + 1] - arr[i] == diff:
            count+=add_to_cnt
            add_to_cnt+=1
        else:
            diff = arr[i + 1] - arr[i]
            add_to_cnt = 1
    return count

def longestArithSeqLength(self, A):
    n = len(A)
    dp = [collections.defaultdict(int) for _ in range(n)]
    res = 0
    for i in range(1, n):
        for j in range(0, i):
            diff = A[i] - A[j]
            dp[i][diff] = dp[j][diff] + 1
            res = max(res, dp[i][diff])
    return res + 1

if __name__ == "__main__":
    print(solution3([1,2,3,8,9,10]))
# 3 - 1
# 4 - 3
# 5 - 6
# 6 - 10
# 7 - 15
# 8 - 21