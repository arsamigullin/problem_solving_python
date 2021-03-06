def solution(amount,coins):
    d = [amount + 1] * (amount + 1)
    d[0] = 0
    for m in range(1, amount + 1):
        for j in range(len(coins)):
            c = coins[j]
            if c <= m:
                d[m] = min(d[m], d[m - c] + 1)
    print(d)
    return -1 if d[amount] > amount else d[amount]

if __name__ == "__main__":
    print(solution(8,[1,3]))
    #print(solution(9,[1,3]))
    #print(solution(6, [1, 2, 3]))
    #print(solution(11,[1,2,5]))
