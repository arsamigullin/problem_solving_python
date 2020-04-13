class MinStack(list):

    def __init__(self):
        """
        initialize your data structure here.
        """

    def push(self, x: int) -> None:
        self.append((x, min(x, self[-1][1] if self else float('inf'))))

    # since list already has this method we call list.pop
    def pop(self) -> None:
        return list.pop(self)[0]

    def top(self) -> int:
        return self[-1][0]

    def getMin(self) -> int:
        return self[-1][1]

