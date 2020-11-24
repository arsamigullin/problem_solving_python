from typing import List


class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        pref = [0] * (len(arr) + 1)
        for i in range(len(arr)):
            pref[i + 1] = pref[i] ^ arr[i]

        # print(pref)
        res = []
        for s, e in queries:
            res.append(pref[s] ^ pref[e + 1])
        return res