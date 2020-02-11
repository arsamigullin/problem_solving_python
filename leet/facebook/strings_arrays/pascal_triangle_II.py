class Solution:
    def getRow(self, rowIndex: int) -> list:
        prev = []
        for i in range(1, rowIndex+2):
            cur = [1] * i
            for j in range(len(cur) - 2):
                cur[j+1] = prev[j]+prev[j+1]
            prev = cur
        return prev