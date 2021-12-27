# the code below is verified in the GeeksforGeeks
# dp top-down
class Solution:

    # Function to return max value that can be put in knapsack of capacity W.
    def knapSack(self, W, weights, vals, n):
        memo = {}
        def recurse(i, leftCap):
            if i >= n or leftCap <= 0:
                return 0
            if (i, leftCap) not in memo:
                if weights[i] > leftCap:
                    memo[(i, leftCap)] = recurse(i + 1, leftCap)
                else:
                    memo[(i, leftCap)] = max(recurse(i + 1, leftCap - weights[i]) + vals[i], recurse(i + 1, leftCap))
            return memo[(i, leftCap)]
        return (0,W)


# One way to understand the fact that "The minimum result of cancellation = the minimum difference between the sum of two groups".
# Say you've already found two groups with smallest difference.
# Group A = [A1, A2, ..., An]
# Group B = [B1, B2, ..., Bm]
# The process we cancel two stones is to arbitrarily pick one from group A and one from Group B.
# If Ai > Bj, then put Ai-Bj into group A.
# If Ai < Bj, then put Ai-Bj into group B.
# If Ai = Bj, then nothing will be put into group A and B.
# We repeat the process until there is only one stone left. You will find the remaining stone is |sum(Group A) - sum(Group B)|.

# this is easy knapsack problem where
# weight = stones
# values = stones

# dp bottom-up
class SolutionBU:

    # Function to return max value that can be put in knapsack of capacity W.
    def knapSack(self, W, weights, vals, n):

        # code here
        memo = [[0] * (W + 1) for _ in range(n + 1)]

        for i in range(1, n + 1):
            for w in range(W, 0, -1):
                if weights[i - 1] > w:
                    memo[i][w] = memo[i - 1][w]
                else:
                    memo[i][w] = max(memo[i - 1][w], vals[i - 1] + memo[i - 1][w - weights[i - 1]])

        return memo[-1][-1]

# turned out we do not have to maintain the 2D-array, 1D-array is enough
# the code is also verified on GeeksforGeeks
class SolutionBU2:

    # Function to return max value that can be put in knapsack of capacity W.
    def knapSack(self, W, weights, vals, n):

        # code here
        memo = [0] * (W + 1)
        for i in range(n):
            for w in range(W, -1, -1):
                if weights[i] <= w:
                    memo[w] = max(memo[w], vals[i] + memo[w - weights[i]])
        return memo[-1]

if __name__ == '__main__':
    s = SolutionBU2()
    s.knapSack(10,[5,3,2,8],[1,6,4,2],4)

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

