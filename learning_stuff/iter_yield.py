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
                    yield from helper(c)
        r = itertools.chain.from_iterable(iter(helper(a)))
        print([v for v in r])
        print(r)


def readfile():
    with open("test.txt") as f:
        yield f.readline()


def read_in_chunks(file_object, chunk_size=1):
    """Lazy function (generator) to read a file piece by piece.
    Default chunk size: 1k."""
    while True:
        data = file_object.read(chunk_size)
        if not data:
            break
        yield data

if __name__ == "__main__":

    with open("test.txt") as f:
        for piece in read_in_chunks(f):
            print(piece)
