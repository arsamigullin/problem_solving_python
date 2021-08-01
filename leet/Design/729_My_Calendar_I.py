class Node:
    # this reduces memory consumption
    # https://book.pythontips.com/en/latest/__slots__magic.html
    __slots__ = 'start', 'end', 'left', 'right'

    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.left = self.right = None

    # this is insertion to the unbalanced BST
    # worst case is O(n^2)
    def insert(self, node):
        lo, hi = node.start, node.end
        if lo >= self.end:
            if not self.right:
                self.right = Node(lo, hi)
                return True
            return self.right.insert(node)
        elif hi <= self.start:
            if not self.left:
                self.left = Node(lo, hi)
                return True
            return self.left.insert(node)
        else:
            # the insertion is not possible because there is an intersection in the intervals
            return False


class MyCalendar:

    def __init__(self):
        self.tree = None

    def book(self, start: int, end: int) -> bool:
        if self.tree is None:
            self.tree = Node(start, end)
            return True
        return self.tree.insert(Node(start, end))

# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)