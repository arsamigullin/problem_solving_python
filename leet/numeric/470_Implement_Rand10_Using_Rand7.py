# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7
import random

def rand7():
    return random.randint(1,7)


# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7

class Solution:

    def rand10(self):
        """
        :rtype: int
        """
        while True:
            row = rand7()
            col = rand7()
            idx = row + (col - 1) * 7
            if idx <= 40:
                return 1 + (idx - 1) % 10


import collections

class SolutionMy:
    '''
    I think this is incorrect solution
    '''
    n = 0
    cnt8 = 0
    cnt10 = 0
    d = collections.defaultdict(int)

    def rand10(self):
        """
        :rtype: int
        """
        self.n += 1
        if self.n == 11:
            self.n = 1
        if 8<= self.n<=10:
            if self.n  == 8:
                return self.cmp(8,9,10)
            elif self.n == 9:
                return self.cmp(8,9,10)
            elif self.n ==10:
                return self.cmp(8,9,10)
        else:
            return rand7()


    def cmp(self, f,s,t):
        if self.d[f] > self.d[s]:
            self.d[s]+=1
            return s
        if self.d[f] > self.d[t]:
            self.d[t] +=1
            return t
        self.d[f]+=1
        return f


if __name__ == '__main__':
    tc = 100000
    res = []
    s = Solution()
    for _ in range(tc):
        res.append(s.rand10())

    for i, el in enumerate(sorted(set(res))):
        print(f"{i+1} {res.count(el)}")
