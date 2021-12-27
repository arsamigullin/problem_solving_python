from collections import defaultdict

class Solution1:
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


class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        h = defaultdict(int)
        bulls = cows = 0
        '''
        secret = 1234
        guess =  4321
        why do we do int(h[s] < 0)? 
        when reaching 3 in secret the h is {1:1,2:1,4:-1,3:-1}
        the value for 3 in the h dict is negative, that means 3 already encountered in the guess
        but now it encountered in secret, that means 3 is cow becuase it is in a secret but has different position in guess
        
        h[g] > 0 says that g encountered earlier in secret, so it also cow
        '''

        for idx, s in enumerate(secret):
            g = guess[idx]
            if s == g:
                bulls += 1
            else:
                cows += int(h[s] < 0) + int(h[g] > 0)
                h[s] += 1
                h[g] -= 1

        return "{}A{}B".format(bulls, cows)


if __name__ == "__main__":
    s = Solution()
    s.getHint("1234", "4321")
    s.getHint("1807", "7810")
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