import collections
from typing import List


class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:

        dp = collections.defaultdict(int)
        for a in A:
            for b in B:
                dp[a+b]+=1
        cnt = 0
        for c in C:
            for d in D:
                    cnt+= dp[-(c+ d)]
        return cnt


class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        #         n = len(A)

        #         sumX={}
        #         sumY={}
        #         for i in range(n):
        #             for j in range(n):
        #                 sa = A[i] + B[j]
        #                 sb = C[i] + D[j]
        #                 if sa not in sumX:
        #                     sumX[sa] =0
        #                 sumX[sa] +=1
        #                 if sb not in sumY:
        #                     sumY[sb] =0
        #                 sumY[sb] +=1

        #         total =0
        #         for k in sumX:
        #             if -k in sumY:
        #                 total += sumX[k] * sumY[-k]
        #         return total
        p, q, r, s = dict(), dict(), dict(), dict()
        for i, j, k, l in zip(A, B, C, D):
            p[i] = p.get(i, 0) + 1
            q[j] = q.get(j, 0) + 1
            r[k] = r.get(k, 0) + 1
            s[l] = s.get(l, 0) + 1

        sumt = dict()
        for i in p:
            for j in q:
                t = i + j
                sumt[t] = sumt.get(t, 0) + p[i] * q[j]

        total = 0
        for i in r:
            for j in s:
                t = i + j
                total += sumt.get(-t, 0) * (r[i] * s[j])

        return total
