#this is wrong
def solution(A):
    n = len(A)

    def find(start, end, diff, is_first=False):

        if start >= end:
            return find(start, end + 1, diff)
        if end >= n:
            return 0
        cur_diff = A[start] - A[end]
        if is_first:
            return find(end, end + 1, cur_diff)
        else:
            print(str(A[start]) + "|" + str(A[end]) + "|" + str(cur_diff) + "|" + str(diff))
            if cur_diff == diff:
                print('here' + str(cur_diff))
                return find(end, end + 1, diff) + 1
            else:
                total = max(find(start, end + 1, diff), find(start + 1, end, cur_diff))
                return total

    res = find(0, 1, A[0] - A[1], True) + 2
    print(res)
    return res

#this is wrong
def solution2(A):
    n = len(A)
    d = dict()
    if n == 2:
        return n
    tot = 0
    for i in range(0, n):
        m = i + 1
        if m >= n:
            break

        while m < n:
            e = m + 1
            em = m
            if e>=n:
                break
            diff = A[i] - A[m]
            key = str(m) + "|" + str(diff)
            if key in d:
                tot = max(d[key], tot)
            else:
                loc_tot = 2
                while e < n:
                    if diff == A[em] - A[e]:
                        print(str(i)+ "|" +str(em) + "|" + str(diff))
                        #print(str(i) + "|" + str(em) + "|" + str(e) + "|"+str(diff))
                        loc_tot += 1
                        em = e
                        e = e + 1
                    else:
                        e+=1
                d[key] = loc_tot
                tot = max(loc_tot, tot)
            m += 1
    return tot

import collections
#this is correct
def solution3(A):
    n = len(A)
    dp = [collections.defaultdict(int) for _ in range(n)]
    res = 0
    # the loop for middle
    for i in range(1, n):
        # this from start to middle
        # initially the difference will be storing at dp[middle][diff]
        # and for example for [9,4,-6,7,2,10] the difference 3 initially will be stored at dp[3][diff], that is,
        # A[3] - A[1] = 7 - 4 = 3
        # further when the middle reaches A[len(A)-1], i.e. 10 we will pull out the count for diff 3 from dp[3][diff]
        # where 3 in dp is index of 7 where we already stored count for difference 3
        for j in range(0, i):
            print(str(j) + "|" + str(i))
            diff = A[i] - A[j]
            #dp[j][diff] - this is previous count
            #dp[i][diff] - this is current count
            dp[i][diff] = dp[j][diff] + 1 # this just takes previous found count and adds 1
            res = max(res, dp[i][diff])
    return res + 1



if __name__ == "__main__":
    solution3([9,4,-6,7,2,10])
    #solution2([20, 1, 15, 3, 10, 5, 8])
    #solution2([44,46,22,68,45,66,43,9,37,30,50,67,32,47,44,11,15,4,11,6,20,64,54,54,61,63,23,43,3,12,51,61,16,57,14,12,55,17,18,25,19,28,45,56,29,39,52,8,1,21,17,21,23,70,51,61,21,52,25,28])
    #solution2([12,28,13,6,34,36,53,24,29,2,23,0,22,25,53,34,23,50,35,43,53,11,48,56,44,53,31,6,31,57,46,6,17,42,48,28,5,24,0,14,43,12,21,6,30,37,16,56,19,45,51,10,22,38,39,23,8,29,60,18])
    #solution2([61,41,59,7,40,46,7,37,70,32,49,58,8,37,59,32,70,53,3,28,17,3,4,66,44,54,6,17,21,70,8,30,28,48,62,13,16,59,47,23,67,26,55,55,71,4,72,51,49,44,59,46,5,0,7,40,67,9,1,39,40,35,47,30,63,49,7,45,47,7,11,3,12,38,72,65,53,5,33,47,67,34,15,4,35,38,53,13,45,23,0,5,62,58,35,6,33,77,30,75])