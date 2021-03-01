# /**
# #  * @return number of ways to make sum s using repeated coins
# #  */
# # public static int coinrep(int[] coins, int s) {
# #     int[] dp = new int[s + 1];
# #     dp[0] = 1;
# #     for (int coin : coins)
# #         for (int i = coin; i <= s; i++)
# #             dp[i] += dp[i - coin];
# #     return dp[s];
# # }

# public int change(int amount, int[] coins) {
#     return change(amount, 0, coins);
# }
# private int change(int balance, int cur, int[] coins) {
#     if(balance == 0) return 1;
#     if(balance<0 || cur == coins.length) return 0;
#     return change(balance-coins[cur], cur, coins) + change(balance, cur+1, coins);
# }

def bruteForce(capacity, i, items):
    if capacity == 0:
        return 1
    if capacity <0 or i == len(items):
        return 0
    return bruteForce(capacity - items[i], i, items) + bruteForce(capacity, i+1, items)


def kanpsack_repeated(items, capacity):
    dp = [0] * (capacity+1)
    dp[0] = 1
    for item in items:
        for i in range(item, capacity+1):
            dp[i] += dp[i-item]
    return dp[capacity]

def kanpsack_non_repeated(items, capacity):
    dp = [[0,[]] for _ in range(capacity+1)]
    dp[0] = 1, [1]
    for item in items:
        for i in range(capacity, item - 1, -1):
            dp[i][0] += dp[i-item][0]
            #if dp[i-item][0] > 0:
            dp[i][1].append(i-item)
    return dp[capacity]


from itertools import groupby
def knapsack_full():
    maxwt = 400

    groupeditems = (
        ("map", 9, 150, 1),
        ("compass", 13, 35, 1),
        ("water", 153, 200, 3),
        ("sandwich", 50, 60, 2),
        ("glucose", 15, 60, 2),
        ("tin", 68, 45, 3),
        ("banana", 27, 60, 3),
        ("apple", 39, 40, 3),
        ("cheese", 23, 30, 1),
        ("beer", 52, 10, 3),
        ("suntan cream", 11, 70, 1),
        ("camera", 32, 30, 1),
        ("t-shirt", 24, 15, 2),
        ("trousers", 48, 10, 2),
        ("umbrella", 73, 40, 1),
        ("waterproof trousers", 42, 70, 1),
        ("waterproof overclothes", 43, 75, 1),
        ("note-case", 22, 80, 1),
        ("sunglasses", 7, 20, 1),
        ("towel", 18, 12, 2),
        ("socks", 4, 50, 1),
        ("book", 30, 10, 2),
    )
    #pre = ([(item, wt, val)] * n for item, wt, val, n in groupeditems)+[]
    items = sum(([(item, wt, val)] * n for item, wt, val, n in groupeditems),[])
    #items = list(([(item, wt, val)] * n for item, wt, val, n in groupeditems))


    def knapsack01_dp(items, limit):
        table = [[0 for w in range(limit + 1)] for j in range(len(items) + 1)]

        for j in range(1, len(items) + 1):
            item, wt, val = items[j - 1]
            for w in range(1, limit + 1):
                if wt > w:
                    table[j][w] = table[j - 1][w]
                else:
                    table[j][w] = max(table[j - 1][w],
                                      table[j - 1][w - wt] + val)

        result = []
        w = limit
        for j in range(len(items), 0, -1):
            was_added = table[j][w] != table[j - 1][w]

            if was_added:
                item, wt, val = items[j - 1]
                result.append(items[j - 1])
                w -= wt

        return result


    bagged = knapsack01_dp(items, maxwt)
    print("Bagged the following %i items\n  " % len(bagged) +
          '\n  '.join('%i off: %s' % (len(list(grp)), item[0])
                      for item, grp in groupby(sorted(bagged))))
    print("for a total value of %i and a total weight of %i" % (
        sum(item[2] for item in bagged), sum(item[1] for item in bagged)))

if __name__ == '__main__':
    #knapsack_full()
    print(kanpsack_repeated([1,2,3],5))
    print(bruteForce(5, 0, [1,2,3]))