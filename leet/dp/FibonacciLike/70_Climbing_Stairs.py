class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2

        first = 1
        sec = 2

        for i in range(3, n + 1):
            first, sec = sec, first + sec

        return sec