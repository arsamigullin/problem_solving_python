from functools import lru_cache


class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        M = (10**9) + 7
        d = {}
        #@lru_cache(None)
        def help(s,i):
            #print(s, i)
            if s==1:
                return 1 if i<=min(1,arrLen-1) else 0
            if (s,i) not in d:

                # S
                out = help(s-1,i)
                if i > 0:
                    # L
                    out += help(s-1,i-1)
                # R
                if i < arrLen-1:
                    out += help(s-1,i+1)
                d[(s,i)] = out
            return d[(s,i)]


        res = help(steps,0)
        print(d)
        return res

if __name__ == '__main__':
    s = Solution()
    s.numWays(4, 2)

class Queue:

    # adds element to the Queue
    def enqueue(self, item):
        pass

    # removes the first item from the queue
    def dequeue(self):
        pass

    # the current size of the Queue
    def size(self):
        pass

    # get the very first item from the Queue without removing it
    def peek(self):
        pass