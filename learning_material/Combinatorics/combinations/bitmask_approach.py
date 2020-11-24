class Solution:
    def combinations(self, items, r):
        combs = []
        n = len(items)
        # that will generate the combination in lexicographically order
        for bitmask in reversed(range(1<<n)):
            if bin(bitmask).count('1') == r:
                # convert bitmask into combination
                # 111 --> "abc", 000 --> ""
                # 110 --> "ab", 101 --> "ac", 011 --> "bc"
                curr = [items[j] for j in range(n) if bitmask&(1<<n-j-1)]
                combs.append(''.join(curr))
        return combs

class GeneratingNextCombination:

    def __init__(self, items, r):
        self.items = items
        self.r = r
        self.n = len(items)
        # generate very first bitmask
        self.bitmask = (1<<self.n) - (1<<self.n - r)


    def nextcombinations(self):
        # convert bitmasks into combinations
        # 111 --> "abc", 000 --> ""
        # 110 --> "ab", 101 --> "ac", 011 --> "bc"
        curr = [self.items[j] for j in range(self.n) if self.bitmask & (1<<self.n-self.r-j)]
        self.bitmask -=1
        # generate next bitmask
        while self.bitmask and bin(self.bitmask).count("1") != self.r:
            self.bitmask -=1

        return ''.join(curr)

    def hasNext(self):
        return  self.bitmask > 0


def all_combinations_using_bits(l):
    n = len(l)
    result = []
    for i in range(1<<n):
        res = []
        for j in range(n):
            # this checks if jth bit is ON in i
            if i&(1<<j):
                res.append(l[j])
        result.append(res[:])
    print(result)

def all_combinations_using_bits_LSOne(n):
    l = list(range(n))
    def LSOne(S):
        return (-S) & S
    result = []
    for i in range(1<<n):
        res = []
        mask = i
        while mask > 0:
            ls = LSOne(mask)
            j = (ls^(ls-1)).bit_length()-1
            res.append(l[j])
            mask -= ls
        result.append(res[:])

    print(result)


if __name__ == '__main__':
    all_combinations_using_bits_LSOne(list(range(8)))
    #all_combinations_using_bits(8)

    #s = Solution()
    #s.combinations("ABCDE", 3)
