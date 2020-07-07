class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        for i in range(1, (n//2)+1):
            if n%i == 0:
                k-=1
            if k == 0:
                return i
        else:
            return  n if k - 1 == 0 else -1

# another approach is to collect all the factors before sqrt(n)
# and then mirrors fo these factors, i.e. n//X[i]
class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        X, i = [], 1
        while i * i <= n:
            if n % i == 0:
                X.append(i)
                if len(X) == k:
                    return i

            i += 1

        l = len(X) - 2 if X[-1] * X[-1] == n else len(X) - 1
        for i in range(l, -1, -1):
            X.append(n // X[i])
            if len(X) == k:
                return X[-1]

        return -1