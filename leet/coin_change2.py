# this solution is wrong because in d we store count of coins that represents m
def solution(amount, coins):
    d = [0]* (amount + 1)
    d[0] = 1
    for m in range(1, amount + 1):
        for c in coins:
            if c <= m:
                d[m] += d[m - c]
    return -1 if d[amount] == 0 else d[amount]

# this is correct because each iteration adds number of way the amount can be represented by
def solution2(amount, coins):
    if amount == 0 and coins is None:
        return 1
    dp = [0] * (amount + 1)
    dp[0] = 1
    for coin in coins:
        for i in range(coin, amount + 1):
            dp[i] += dp[i - coin]
    return dp[amount]

if __name__ == "__main__":
    print(solution(5,[1,2,5]))
