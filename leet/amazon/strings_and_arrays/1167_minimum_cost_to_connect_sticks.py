import collections
import heapq
from typing import List


class Solution2:
    def connectSticks(self, sticks: List[int]) -> int:
        if not sticks or len(sticks) == 1:
            return 0
        heapq.heapify(sticks)
        cost = 0
        while len(sticks) > 1:
            first = heapq.heappop(sticks)
            sec = heapq.heappop(sticks)
            tot = first + sec
            cost += tot
            heapq.heappush(sticks, tot)
        return cost


from heapq import heappush, heappop, heapify

# this is the same but more clear solution
class Solution1:
    def connectSticks(self, sticks: List[int]) -> int:
        res = 0

        heapify(sticks)

        while len(sticks) > 1:
            a, b = heappop(sticks), heappop(sticks)
            c = a + b
            res += c
            heappush(sticks, c)
        return res


# the fastest solution

    def connectSticks(self, sticks: List[int]) -> int:
        if len(sticks) == 1: return 0
        sticks.sort()
        res = sum(sticks[:2])
        dq = collections.deque([res])
        i = 2
        while i < len(sticks):
            if sticks[i] <= dq[0] or len(dq) == 1:
                if i + 1 < len(sticks) and sticks[i + 1] <= dq[0]:
                    combo = sticks[i] + sticks[i + 1]
                    i += 2
                else:
                    combo = sticks[i] + dq[0]
                    dq.popleft()
                    i += 1
            else:
                if dq[1] <= sticks[i]:
                    combo = dq[0] + dq[1]
                    dq.popleft()
                    dq.popleft()
                else:
                    combo = sticks[i] + dq[0]
                    dq.popleft()
                    i += 1
            dq.append(combo)
            res += combo

        while len(dq) > 1:
            combo = dq[0] + dq[1]
            dq.popleft()
            dq.popleft()
            dq.append(combo)
            res += combo
        return res

if __name__ == '__main__':
    s = Solution()
    s.connectSticks([1,8,3,5])