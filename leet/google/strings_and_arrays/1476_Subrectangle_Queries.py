from typing import List


class SubrectangleQueries:
    '''
    Here wer are actually not going to change anything
    '''
    def __init__(self, rectangle: List[List[int]]):
        self.rectangle = rectangle
        self.stack = []
        self.n = 0

    def updateSubrectangle(self, row1: int, col1: int, row2: int, col2: int, newValue: int) -> None:
        # we will just collect the modification and coordinates of the modificaiton
        self.stack.append((row1, col1, row2, col2, newValue))
        self.n += 1

    def getValue(self, row: int, col: int) -> int:
        # the we iterating over the modification and if the reuqested coordinates lies
        # in one of the modifications, we return it
        for i in range(self.n - 1, -1, -1):
            tmp = self.stack[i]
            if tmp[0] <= row <= tmp[2] and tmp[1] <= col <= tmp[3]:
                return tmp[4]
        return self.rectangle[row][col]