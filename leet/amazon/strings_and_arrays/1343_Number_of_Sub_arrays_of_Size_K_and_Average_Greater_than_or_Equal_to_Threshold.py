from typing import List


class Solution1:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:

        tot = sum(arr[:k])
        cnt = 0
        for i in range(1, len(arr) - k + 1):
            if tot // k >= threshold:
                cnt += 1
            tot -= arr[i - 1]
            tot += arr[i + k - 1]
        if tot // k >= threshold:
            cnt += 1
        return cnt
