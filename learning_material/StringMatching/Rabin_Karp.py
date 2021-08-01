
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



class RabinKarp:
    def find_matching_index(self, T: str, P: str) -> int:

        if len(P) == 0:
            return 0
        n = len(T)
        m = len(P)
        p = 131
        M = 10 ** 9 + 7
        Pow = [0] * max(n, m)
        h = [0] * max(n, m)

        def prepare():
            Pow[0] = 1
            for i in range(1, n):
                Pow[i] = (Pow[i - 1] * p) % M
            return  Pow

        def computeRollingHash(T,Pow):
            h[0] = 0
            for i in range(n):
                if i > 0:
                    h[i] = h[i - 1];
                h[i] = (h[i] + (ord(T[i]) * Pow[i]) % M) % M

        def extEuclid(a, b):
            xx, yy = 0, 1
            x, y = 1, 0
            while b != 0:
                q = a // b
                a, b = b, a % b
                x, xx = xx, x - q * xx
                y, yy = yy, y - q * yy
            return a, x, y

        def modInverse(b, m):
            d, x, y = extEuclid(b, m)
            if d != 1:
                return -1
            return (x + m) % m

        def hash_fast(L, R, Pow):
            if L == 0:
                return h[R]
            ans = ((h[R] - h[L - 1]) % M + M) % M
            ans = (ans * modInverse(Pow[L], M)) % M
            return ans

        Pow = prepare()
        computeRollingHash(T, Pow)
        # hash of the Pattern
        hP = 0;
        for i in range(m):
            hP = (hP + ord(P[i]) * Pow[i]) % M
        for i in range(n - m + 1):
            if hash_fast(i, i + m - 1, Pow) == hP:
                return i
        return -1
# problem to check on
# https://leetcode.com/problems/implement-strstr/submissions/
def RabinKarpChecking(T, P):
    n = len(T)
    m = len(P)
    p = 31
    M = 10**9+7
    Pow = [0] * n
    h = [0]*n

    def get_pow():
        Pow[0]=1
        for i in range(1,n):
            Pow[i] = (Pow[i-1]*p)%M
        return Pow

    def computeHash(Pow):
        for i in range(n):
            if i > 0:
                h[i] = h[i-1]
            h[i] = (h[i] + (ord(T[i])*Pow[i])%M)%M

    def extEuclid(a,b):
        x, u = 0, 1
        y, v = 1, 0
        while b!=0:
            q = a//b
            a, b = b, a%b
            x, u = u, x-q*u
            y, v = v, y-1*v
        return a,x,y

    def modInverse(p,m):
        d,x,y = extEuclid(p,m)
        if d!=1:
            return -1
        return (x+m)%m

    def fast_hash(L,R,Pow):
        if L == 0:
            return h[R]
        ans = (h[R] - h[L-1] + M) % M
        ans = (ans * modInverse(Pow[L], M))%M
        return ans

    Pow = get_pow()
    computeHash(Pow)
    hP = 0
    for i in range(m):
        hP=(hP+(ord(P[i])*Pow[i]))%M

    for i in range(n-m+1):
        if fast_hash(i, i+m) == hP:
            return i
    return -1


if __name__ == '__main__':

    P = "abcabcabcabc"
    T = "abcabcabcabc"
    rab_karp = RabinKarp()
    rab_karp.find_matching_index(T, P)


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



