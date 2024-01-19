import collections
from typing import List


class SolutionDFS:
    def canReach(self, arr: List[int], start: int) -> bool:
        dp = [0] * len(arr)

        def dfs(i):
            if arr[i] == 0:
                return True
            if dp[i] == 1:
                return False
            dp[i] = 1
            for j in [i - arr[i], i + arr[i]]:
                if 0 <= j < len(arr):
                    if dfs(j):
                        return True
            return False

        return dfs(start)


class SolutionBFS:
    def canReach(self, arr: List[int], start: int) -> bool:

        dp = [0] * len(arr)
        q = collections.deque([start])
        while q:
            i = q.popleft()
            if arr[i] == 0:
                return True
            if dp[i] == 1:
                continue
            dp[i] = 1
            if 0 <= i - arr[i] < len(arr):
                q.append(i - arr[i])
            if 0 <= i + arr[i] < len(arr):
                q.append(i + arr[i])

        return False


class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        n = len(arr)
        dp = [0] * n

        def helper(i):
            if arr[i] == 0:
                return True
            if dp[i] > 0:
                return False
            dp[i] = 1
            if i + arr[i] < n:
                if helper(i + arr[i]):
                    return True
            if i - arr[i] >= 0:
                if helper(i - arr[i]):
                    return True
            return False

        return helper(start)

# O(n)
class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:

        q = deque([start])
        n = len(arr)
        visited = {start}
        while q:
            i = q.popleft()
            if 0 == arr[i]:
                return True
            r = i + arr[i]
            l = i - arr[i]
            if 0 <= r < n and r not in visited:
                q.append(r)
                visited.add(r)
            if 0 <= l < n and l not in visited:
                q.append(l)
                visited.add(l)
        return False


if __name__ == '__main__':
    s = Solution4()
    s.canReach([4,2,3,0,3,1,2], 5)

