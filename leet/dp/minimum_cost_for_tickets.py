from functools import lru_cache

def solution(days, cost):
    if len(days) == 0:
        return 0
    dp = [cost[2]] * len(days)
    tot1 = cost[0]
    tot7 = cost[1]
    tot30 = cost[2]
    days_pass = [1,7,30]
    dp[-1] = cost[0]
    day_7 = days[-1] - 7 + 1
    day_30 = days[-1] - 30 + 1
    for i in range(len(days)-2, -1, -1):

        for c, p in zip(cost, days_pass):
            if p == 1:
                tot1 = dp[i+1] + c
            elif p == 7:
                if days[i] < day_7:
                    day_7 = days[i] - p + 1
                    tot7 = dp[i+1] + c
            else: #p == 30
                if days[i] < day_30:
                    day_30 = days[i] - p + 1
                    tot30 = dp[i+1] + c

        dp[i] = min(tot1, tot7, tot30)
    return  dp[-1]


def mincostTickets(days, costs):
    N = len(days)
    durations = [1, 7, 30]

    @lru_cache(None)
    def dp(i): # How much money to do days[i]+
        if i >= N: return 0

        ans = float('inf')
        j = i
        for c, d in zip(costs, durations):
            while j < N and days[j] < days[i] + d:
                j += 1
            ans = min(ans, dp(j) + c)
            print('duration '+str(d)+' ans ' + str(ans) + ' days ' + str(days[i]))
        #print('ans ' + str(ans) + ' days ' + str(days[i]) + ' i ' + str(i))
        return ans

    return dp(0)

if __name__ == "__main__":
    #mincostTickets([1,4,6,7,8,20], [2,7,15])
    mincostTickets([1, 2, 4, 5, 6, 9, 10, 12, 14, 15, 18, 20, 21, 22, 23, 24, 25, 26, 28], [3, 13, 57])
    #solution([1,2,4,5,6,9,10,12,14,15,18,20,21,22,23,24,25,26,28], [3,13,57])