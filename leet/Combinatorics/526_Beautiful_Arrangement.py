class Solution:
    def countArrangement(self, N: int) -> int:
        visited = [False] * (N + 1)
        count = 0

        def calculate(pos):
            nonlocal count
            if pos > N:
                count += 1
            for i in range(1, N + 1):
                if not visited[i] and (pos % i == 0 or i % pos == 0):
                    visited[i] = True
                    calculate(pos + 1)
                    visited[i] = False

        calculate(1)
        return count

if __name__ == '__main__':
    s = Solution()
    s.countArrangement(5)