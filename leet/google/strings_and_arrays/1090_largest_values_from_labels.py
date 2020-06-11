from typing import List


class Solution:
    def largestValsFromLabels(self, values: List[int], labels: List[int], num_wanted: int, use_limit: int) -> int:
        values = sorted([(i, v) for i, v in enumerate(values)], reverse=True, key=lambda x: x[1])
        d = {v: use_limit for v in set(labels)}
        tot = 0
        for i in range(len(values)):
            ind, val = values[i]
            if d[labels[ind]] > 0:
                tot += val
                d[labels[ind]] -= 1
                num_wanted -= 1
            if num_wanted == 0:
                break
            i += 1
        return tot


