
# the approach seem to be wrong
class RabinKarp:

    def findmatch(self, P, T):
        n = len(T) # text
        m = len(P) # pattern
        modulus = 2**32
        d = 54324
        h = pow(d, m-1, modulus)
        p = 0
        t = 0
        # initializtion
        for i in range(m):
            p = (d*p + ord(P[i]))%modulus
            t = (d*t + ord(T[i]))%modulus
        for i in range(n-m):
            if p == t:
                if P == T[i:i+m]:
                    print('match found')
            else:
                # formula in Kormen's textbook
                t = ((d*(t - ord(T[i])*h)) + ord(T[i+m])) % modulus
        if p == t:
            print('match found')

if __name__ == '__main__':
    s = RabinKarp()
    s.findmatch("ab","fdghgfabab")