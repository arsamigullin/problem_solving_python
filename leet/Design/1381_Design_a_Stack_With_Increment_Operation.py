class CustomStack:

    def __init__(self, maxSize: int):
        self.stack = []
        self.size = maxSize

    def push(self, x: int) -> None:
        if len(self.stack) < self.size:
            self.stack.append(x)

    def pop(self) -> int:
        return self.stack.pop() if self.stack else -1

    def increment(self, k: int, val: int) -> None:
        for i in range(min(len(self.stack),k)):
            self.stack[i]+=val


class CustomStack1:

    def __init__(self, maxSize: int):
        self.stack = []
        self.inc = []
        self.ms = maxSize

    def push(self, x: int) -> None:
        if len(self.stack) < self.ms:
            self.stack.append(x)
            self.inc.append(0)

    def pop(self) -> int:
        if self.stack:
            # when popping
            # we extract values from stack and inc
            base = self.stack.pop()
            inc = self.inc.pop()
            # NOTE: since the previous item is supposed to be incremented at inc (but we did not do that to
            # save running time) we increment the previous item to the popped value inc
            if self.inc:
                self.inc[-1] += inc
            return base + inc
        return -1

    def increment(self, k: int, val: int) -> None:
        if self.inc:
            # when incrementing we do store val to increment at the min(k, len(inc))-1 index
            self.inc[min(k, len(self.inc)) - 1] += val

if __name__ == '__main__':
    s = CustomStack1(3)
    params = [[1], [2], [], [2], [3], [4], [5, 100], [2, 100], [], [], [], []]
    for i, oper in enumerate(["push", "push", "pop", "push", "push", "push", "increment", "increment", "pop", "pop", "pop", "pop"]):
        if oper == "push":
            s.push(params[i][0])
        elif oper == "pop":
            s.pop()
        elif oper == "increment":
            s.increment(params[i][0],params[i][1])



# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)