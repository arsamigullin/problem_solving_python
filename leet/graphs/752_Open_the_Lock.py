import collections
from typing import List


class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:

        def neighbors(node):
            for i in range(4):
                x = int(node[i])
                for d in (-1, 1):
                    nei = (x + d) % 10
                    print(node[:i] + str(nei) + node[i + 1:])
                    yield node[:i] + str(nei) + node[i + 1:]

        dead = set(deadends)
        q = collections.deque([('0000', 0)])
        seen = set()
        while q:
            node, level = q.popleft()
            if node == target: return level
            if node in dead:
                continue
            # we cannot put it here because we will omit its children
            #if node in seen:
            #    continue
            for nei in neighbors(node):
                if nei not in seen:
                    seen.add(nei)
                    q.append((nei, level + 1))
        return -1


