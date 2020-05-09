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