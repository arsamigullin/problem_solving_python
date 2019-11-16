#2d DP solution. Time complexity O(target*d*f)
class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        # dp[i][j] -> num of ways to reach target = i with j dices
        dp = [[0 for i in range(d + 1)] for j in range(target + 1)]
        dp[0][0] = 1

        for k in range(1, target + 1):
            for i in range(1, d + 1):
                for j in range(1, min(f + 1, k + 1)):
                    dp[k][i] = (dp[k][i] + dp[k - j][i - 1]) % (1e9 + 7)
        return int(dp[target][d] % (1e9 + 7))



def numRollsToTarget(d: int, f: int, target: int) -> int:
    if target > d * f:
        return 0

    # dp[i][j] -> num of ways to reach target = i with j dices
    # i.e. here we are storing target/dice relationship. The values are ways to reach the target with dices
    dp = [[0 for i in range(d + 1)] for j in range(target + 1)]
    dp[0][0] = 1


    for k in range(1, target + 1): # gradually increasing target strating from 1
        # for each dice/target. Basically this dice. Min here because there is no use to consider all the dices if
        # target less than dices
        for i in range(1, min(d + 1, k + 1)): # gradually increasing faces strating from 1
            # for each face/target. Basically this face. Min here because there is no use to consider all the faces if
            # target less than faces
            for j in range(1, min(f + 1, k + 1)):
                # with increasing faces we increasing the same value dp[k][i] with previous
                dp[k][i] = (dp[k][i] + dp[k - j][i - 1]) % (1e9 + 7)
    return int(dp[target][d] % (1e9 + 7))

if __name__ == "__main__":
    numRollsToTarget(3,6,7)

# rows - target,
# column - dices
# values - num of ways
# face is substracted from target
#    0  1  2  3 - dices
#0 [[1, 0, 0, 0],
#1 [0, 1.0, 0, 0],
#2 [0, 1.0, 1.0, 0],
#3 [0, 1.0, 2.0, 1.0],
#4 [0, 1.0, 3.0, 3.0],
#5 [0, 1.0, 4.0, 6.0],
#6 [0, 1.0, 5.0, 10.0],
#7 [0, 0.0, 6.0, 15.0]]
#t
#a
#r
#g
#e
#t