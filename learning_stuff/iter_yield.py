import typing


class NestedInteger:
    def __init__(self):
        self

    def isInteger(self) -> bool:
        pass

    def getInteger(self) -> int:
        pass

    def getList(self):
        pass

    def setData(self, val):
        pass



import itertools
class Solution:
    def __init__(self):
        a = ['v','ab','f']
        def helper(arr):
            for c in arr:
                if len(c) == 1:
                    yield c[0]
                else:
                    yield helper(c)
        r = itertools.chain.from_iterable(iter(helper(a)))
        print([v for v in r])
        print(r)


if __name__ == "__main__":
    s = Solution()