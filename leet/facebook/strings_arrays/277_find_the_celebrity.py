# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:



class Solution:
    '''
    suppose we have people[0,1,2,3]
    if 0 knows 1, 0 cannot be celebrity
    if 0 does not know 1, 0 can potentially be the celebrity
    '''
    def findCelebrity(self, n: int) -> int:
        cand = 0
        for i in range(1, n):
            # find potential celebrity
            if knows(cand, i):
                cand = i

        for i in range(n):
            if i == cand:
                continue
            # if potential celebrity knows someone or someone does not know celebrity
            # this is not a celebrity
            if knows(cand, i) or not knows(i, cand):
                return -1
        return cand