class Solution:
    def __init__(self):
        self.res = []

    def combine(self, n: int, k: int) -> list:
        for i in range(1, n - k + 1):
            for j in range(i + 1, n + 1):
                cnt = 0
                tres = [i]
                while cnt < k - 1:
                    tres.append(j + cnt)
                    cnt += 1
                self.res.append(tres)
        return self.res

if __name__ == "__main__":
    s = Solution()
    s.combine(4,2)