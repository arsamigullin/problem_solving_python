from collections import deque
from math import inf
from typing import List


class Solution:
    def timeTaken(self, arrival: List[int], state: List[int]) -> List[int]:
        n = len(arrival)
        ret = [0] * n

        # state variables
        q_enter = deque()  # (time, pid)
        q_exit = deque()  # (time, pid)

        for pid, arrive_time in enumerate(arrival):
            (q_exit if state[pid] == 1 else q_enter).append(pid)

        t = 0
        while q_enter or q_exit:
            t_next = min(
                arrival[q_enter[0]] if q_enter else inf,
                arrival[q_exit[0]] if q_exit else inf,
            )

            t = max(t_next, t)

            while q_exit and arrival[q_exit[0]] <= t:
                pid = q_exit.popleft()
                ret[pid] = t
                t += 1

            while q_enter and arrival[q_enter[0]] <= t:
                pid = q_enter.popleft()
                ret[pid] = t
                t += 1

        return ret

if __name__ == '__main__':
    s = Solution()
    s.timeTaken([0,1,1,2,4], [0,1,0,0,1])