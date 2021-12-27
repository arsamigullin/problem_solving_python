from typing import List


class Solution:
    def findReplaceString(self, orig: str, indices: List[int], sources: List[str], targets: List[str]) -> str:

        to_add = []
        prev = 0
        for i, s, t in sorted(zip(indices, sources, targets), key=lambda x: x[0]):
            to_add.append(orig[prev:i])
            if orig[i:i + len(s)] == s:
                to_add.append(t)
                prev = i + len(s)
            else:
                prev = i
        to_add.append(orig[prev:len(orig)])
        return ''.join(to_add)

