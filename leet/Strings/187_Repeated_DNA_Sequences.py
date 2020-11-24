import collections
from typing import List

# sliding window

class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        part = collections.deque(s[:10])
        visited = collections.defaultdict(int)
        visited[''.join(part)] = 1
        for i in range(10, len(s)):
            part.popleft()
            part.append(s[i])
            key = ''.join(part)
            visited[key] += 1

        return [k for k, v in visited.items() if v > 1]


class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        if s is None or len(s) == 0:
            return []

        n = len(s)
        result = set()
        hashset = set()
        for i in range(n - 10 + 1):
            sub = s[i:i + 10]
            if sub in hashset:
                result.add(sub)

            hashset.add(sub)

        return list(result)