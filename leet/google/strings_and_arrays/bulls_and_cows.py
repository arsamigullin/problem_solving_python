from collections import defaultdict

class Solution:
    def getHint(self, secret, guess):
        bull = cow = 0
        s = defaultdict(int) # secret hashtable
        g = defaultdict(int) # guess hashtable
        for si, gi in zip(secret, guess):
            if si == gi:
                bull += 1
            else:
                s[si] += 1
                g[gi] += 1
    # since we consider only items that are in secret we take min
        cow += sum(min(s[k], g[k]) for k in g)
        return '%dA%dB' % (bull, cow)

if __name__ == "__main__":
    s = Solution()
    s.getHint("1123","0111")


class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        b = 0
        c = 0
        ds = {}
        dg = {}
        for i, v in enumerate(secret):
            ds[v] = ds.get(v, 0) + 1
        for i, v in enumerate(guess):
            dg[v] = dg.get(v, 0) + 1

        for s, g in zip(secret, guess):
            if s == g:
                b += 1
                ds[s] -= 1
                dg[g] -= 1

        for k, v in dg.items():
            if k in ds:
                c += min(ds[k], v)

        return f"{b}A{c}B"