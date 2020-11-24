
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



MAX_N = 200010
p = 131
M = 10**9+7
Pow = [0] * MAX_N
h = [0] * MAX_N

def computeRollingHash(T):
  n = len(T)

  Pow[0] = 1
  for i in range(1, n):
    Pow[i] = (Pow[i-1]*p) % M
  h[0] = 0
  for i in range(n):
    if i != 0:
      h[i] = h[i-1];
    h[i] = (h[i] + (ord(T[i])*Pow[i]) % M) % M


def extEuclid(a, b):
  xx, yy = 0, 1
  x, y = 1, 0
  while b != 0:
    q = a//b
    a, b = b, a%b
    x, xx = xx, x-q*xx
    y, yy = yy, y-q*yy
  return a, x, y


def modInverse(b, m):
  d, x, y = extEuclid(b, m)
  if d != 1:
    return -1
  return (x+m)%m


def hash_fast(L, R):
  if L == 0:
    return h[R]
  ans = ((h[R] - h[L-1]) % M + M) % M
  ans = (ans * modInverse(Pow[L], M)) % M
  return ans


if __name__ == '__main__':

    P = "abcabcabcabc"
    T = "abcabcabcabc"
    n = len(T)
    m = len(P)

    computeRollingHash(T)
    hP = 0
    for i in range(m):
        hP = (hP + ord(P[i])*Pow[i]) % M
    freq = 0
    for i in range(n-m+1):
        if hash_fast(i, i+m-1) == hP:
            freq += 1
    print('Rabin-Karp, #match = %d' % freq)

if __name__ == '__main__':
    s = RabinKarp()
    s.findmatch("ab","fdghgfabab")