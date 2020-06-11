import collections
from typing import List


class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        s = []
        i = 0
        for item in pushed:
            s.append(item)
            while s and s[-1]==popped[i]:
                i+=1
                s.pop()
        return len(s) == 0



class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        s = []
        i = 0, 0
        popped = collections.deque(popped)

        while i < len(pushed):
            # we populate stack while current pushed item is not equal popped
            if not s or s[-1] != popped[0]:
                s.append(pushed[i])
                i += 1
            # but if they are not equal we pop them out from both
            else:
                s.pop()
                popped.popleft()

        # if stack is still not empty we compare elements from two lists
        while s:
            if s.pop() != popped.popleft():
                return False
        return True

class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        s = []
        i = 0
        for item in pushed:
            s.append(item)
            while s and s[-1]==popped[i]:
                i+=1
                s.pop()
        return len(s) == 0


if __name__ == '__main__':
    s = Solution()
    s.validateStackSequences([1,2,3,4,5],[4,3,5,2,1])