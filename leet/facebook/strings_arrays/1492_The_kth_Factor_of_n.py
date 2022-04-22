class Solution1:
    def kthFactor(self, n: int, k: int) -> int:
        for i in range(1, (n//2)+1):
            if n%i == 0:
                k-=1
            if k == 0:
                return i
        else:
            return  n if k - 1 == 0 else -1

class Solution2:
    def kthFactor(self, n: int, k: int) -> int:
        # for n = 1024 and k = 9
        # n is perfect square, their root is 32
        # iterating from 1 to 32 gives us
        # divs = [1, 2, 4, 8, 16, 32]
        divs = []
        sqrt = int(n ** 0.5)
        for i in range(1, sqrt+1):
            if n % i == 0:
                divs.append(i)
                k-=1
            if k==0:
                return i
        # the full list of the divisors [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]
        # square root 32 is the middle in the all divisors
        # at this point we've counted all divisors until 32
        # this if is only to adjust index when doing len(divs)-k]
        if sqrt*sqrt == n:
            k+=1
        # here we search for the mirrored factor
        # at this point k=4, len(divs) is 6 and 6-4=2. So we want to find
        # the mirror factor of the divs[2] by doing b//divs[2]
        return n//divs[len(divs)-k] if k<=len(divs) else -1

if __name__ == '__main__':
    s = Solution2()
    s.kthFactor(1024, 9)
    d = []
    for i in range(1,1024):
        if 1024%i == 0:
            d.append(i)
    print(d)