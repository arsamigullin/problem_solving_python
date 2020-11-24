# https://leetcode.com/problems/task-scheduler/
# Observations
# Each tasks are represented by Letters
# The order of obtaining the tasks does not matter
# Algo
# 1. We count the tasks and store in map
# 2. we sort the map so the task with greater count will be at 25 index
# 3. while the latest item is not 0 we decrease by 1 the n consecutive elements of the map starting from the end
# 4. we sort map again to obtain the tasks with the most count
from typing import List


class Solution1:
    def leastInterval(self, tasks: list, n: int) -> int:
        tasks_map = [0] * 26
        total = 0
        #1
        for i, v in enumerate(tasks):
            tasks_map[ord(v) - 65] += 1
        #2
        tasks_map.sort()
        #3
        while tasks_map[25] != 0:
            i = 0
            while i <= n:
                if tasks_map[25] == 0:
                    break
                if i < 26 and tasks_map[25 - i]:
                    tasks_map[25 - i] -= 1
                total += 1
                i += 1
            tasks_map.sort()

        return total


# still not clear about this
import collections
class SolutionShort:
    def leastInterval(self, tasks: list, n: int) -> int:
        d = collections.Counter(tasks)
        counts = list(d.values())
        longest = max(counts)
        ans = (longest - 1) * (n + 1) + counts.count(longest)
        return max(len(tasks), ans)


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        m = [0] * 26
        for t in tasks:
            m[ord(t) - 65] += 1

        m.sort()
        total = 0
        while m[25] != 0:
            for i in range(n+1):
                if m[25] == 0: break
                if i < 26 and m[25 - i]:
                    m[25-i] -= 1
                total += 1
            m.sort()
        return total


if __name__ == "__main__":
    s=Solution()
    s.leastInterval(["A","A","A","A","A","A","B","C","D","E","F","G"],2)
    s.leastInterval(["A","A","A","B","B","B", "C","C","C", "D", "D", "E"],2)

    s.leastInterval(["A","A","A","B","B","B"],2)