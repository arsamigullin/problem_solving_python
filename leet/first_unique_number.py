from typing import List


class DLL:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None


class FirstUnique:

    def __init__(self, nums: List[int]):
        self.d = {}
        self.tail = self.head = DLL(0)

        for n in nums:
            self.addNode(n)

    def addNode(self, n):
        if n in self.d:
            if self.d[n] is None:
                return
            prev = self.d[n].prev
            nxt = self.d[n].next
            if prev is not None:
                prev.next = nxt
            if nxt is not None:
                nxt.prev = prev
            else:
                self.tail = prev
            self.d[n] = None
        else:
            node = DLL(n)
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
            self.d[n] = node

    def showFirstUnique(self) -> int:
        return self.head.next.val if self.head.next is not None else -1

    def add(self, value: int) -> None:
        self.addNode(value)


from collections import Counter, deque


class FirstUnique:

    def __init__(self, nums: List[int]):
        self.c = Counter(nums)
        self.d = deque(nums)

    def showFirstUnique(self) -> int:
        while self.d and self.c[self.d[0]] != 1:
            self.d.popleft()
        return self.d[0] if self.d else -1

    def add(self, value: int) -> None:
        self.c[value] += 1
        self.d.append(value)


if __name__ == '__main__':
    #["FirstUnique", "showFirstUnique", "add", "showFirstUnique", "add", "showFirstUnique", "add", "showFirstUnique"]
    #[[[2, 3, 5]], [], [5], [], [2], [], [3], []]
    s = FirstUnique([2, 2, 2, 2])
    s.showFirstUnique()
    s.add(5)
    s.showFirstUnique()
    s.add(2)
    s.showFirstUnique()
    s.add(3)
    s.showFirstUnique()
