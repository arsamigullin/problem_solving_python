from collections import *


class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue1 = deque()
        self.queue2 = deque()
        self.topitem = None

    def push(self, x: int) -> None:
        self.topitem = x
        self.queue1.append(x)
        print('1')


    def pop(self) -> int:
        print('2')
        while len(self.queue1) > 1:
            self.topitem = self.queue1.popleft()
            self.queue2.append(self.topitem)
        last = self.queue1.popleft()
        self.queue1, self.queue2 = self.queue2, self.queue1

        return last


    def top(self) -> int:
        print('3')
        return self.topitem


    def empty(self) -> bool:
        print('4')
        return len(self.queue1) == 0

if __name__ == "__main__":
    s = MyStack()
    s.push(1)
    s.push(2)
    s.top()
    print(s.pop())
    print(s.empty())