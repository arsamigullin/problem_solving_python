class BinaryIndexedTree:
    def __init__(self, n):
        self.n = n
        self.c = [0] * (n + 1)

    def update(self, x, delta):
        while x <= self.n:
            self.c[x] += delta
            x += x & -x

    def query(self, x):
        s = 0
        while x:
            s += self.c[x]
            x -= x & -x
        return s

class FTree:
    def __init__(self, f):
        self.n = len(f)
        self.ft = [0] * (self.n + 1)

        for i in range(1, self.n + 1):
            self.ft[i] += f[i - 1]
            if i + self.lsone(i) <= self.n:
                self.ft[i + self.lsone(i)] += self.ft[i]

    def lsone(self, s):
        return s & (-s)

    def query(self, i, j):
        if i > 1:
            return self.query(1, j) - self.query(1, i - 1)

        s = 0
        while j > 0:
            s += self.ft[j]
            j -= self.lsone(j)

        return s

    def update(self, i, v):
        while i <= self.n:
            self.ft[i] += v
            i += self.lsone(i)

    def select(self, k):
        p = 1
        while (p * 2) <= self.n: p *= 2

        i = 0
        while p > 0:
            if i + p < len(self.ft) and k > self.ft[i + p]:
                k -= self.ft[i + p]
                i += p
            p //= 2

        return i + 1

class RUPQ:
    def __init__(self, n):
        self.ftree = FTree([0] * n)

    def query(self, i):
        return self.ftree.query(1, i)

    def update(self, i, j, v):
        self.ftree.update(i, v)
        self.ftree.update(j + 1, -v)

class RURQ:
    def __init__(self, n):
        self.f = FTree([0] * n)
        self.r = RUPQ(n)

    def query(self, i, j):
        if i > 1:
            return self.query(1, j) - self.query(1, i - 1)
        return self.r.query(j) * j - self.f.query(1, j)

    def update(self, i, j, v):
        self.r.update(i, j, v)
        self.f.update(i, v * (i - 1))
        self.f.update(j + 1, -1 * v * j)

if __name__ == '__main__':
    f = [2,3,6,5,2,3]
    freq = [0] * len(f)
    for i, num in enumerate(f):
        freq[num-1]+=1
    print(freq)
    ft = FTree(freq)
    bi = BinaryIndexedTree(len(f))
    for num in f:
        bi.update(num, 1)

    print(ft.query(3,5))
    print(bi.query(5) - bi.query(2))



    f = [0, 1, 0, 1, 2, 3, 2, 1, 1, 0]
    ft = FTree(f)
    print(ft.query(1, 6) == 7)
    print(ft.query(1, 3) == 1)
    print(ft.select(7) == 6)
    ft.update(5, 1)
    print(ft.query(1, 10) == 12)

    r = RUPQ(10)
    r.update(2, 9, 7)
    r.update(6, 7, 3)
    print(r.query(1) == 0)
    print(r.query(2) == 7)
    print(r.query(3) == 7)
    print(r.query(4) == 7)
    print(r.query(5) == 7)
    print(r.query(6) == 10)
    print(r.query(7) == 10)
    print(r.query(8) == 7)
    print(r.query(9) == 7)
    print(r.query(10) == 0)

    r = RURQ(10)
    r.update(2, 9, 7)
    r.update(6, 7, 3)
    print(r.query(3, 5) == 21)
    print(r.query(7, 8) == 17)