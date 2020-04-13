import collections

class Solution:
    '''
    NOTE: we are asked to find min value to turn string t from s
    this means we need to count the letters that are absent in t
    '''
    def minSteps(self, s: str, t: str) -> int:
        ds = {}
        dt = {}
        for cs, ct in zip(s,t):
            ds[cs] = ds.get(cs,0)+1
            dt[ct] = dt.get(ct,0)+1
        cnt = 0
        for k, v in ds.items():
            if k in dt:
                diff = ds[k]-dt[k]
                cnt += diff if diff > 0 else 0
            else:
                cnt+=ds[k]
        return cnt

# the short solution
class Solution:
    def minSteps(self, s: str, t: str) -> int:
        c1 = collections.Counter(s)
        c2 = collections.Counter(t)
        return sum((c1 - c2).values())