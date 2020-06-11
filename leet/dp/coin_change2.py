# this solution is wrong because in d we store count of coins that represents m
def solution(amount, coins):
    d = [0]* (amount + 1)
    d[0] = 1
    for m in range(1, amount + 1):
        for c in coins:
            if c <= m:
                d[m] += d[m - c]
    return -1 if d[amount] == 0 else d[amount]

# this is correct because each iteration adds number of ways the amount can be represented by
#You are given coins of different denominations and a total amount of money.
# Write a function to compute the number of combinations that make up that amount. You may assume that you have infinite number of each kind of coin.
def solution2(amount, coins):
    if amount == 0 and coins is None:
        return 1
    dp = [0] * (amount + 1)
    dp[0] = 1
    '''
    consider example 5,  [1,2,5]
    dp = [1,0,0,0,0,0]
    we iterate over coins first
    and then we find the ways to represent each denomination till 5 using only the current coin
    the ways for future coin will be add up to the ways of previous coins
    
    '''

    for coin in coins:
        # here we define
        for target in range(coin, amount + 1):
            # how many ways the target can be represented by given coin
            dp[target] += dp[target - coin]
    return dp[amount]

if __name__ == "__main__":
    print(solution2(5,[1,2,5]))
