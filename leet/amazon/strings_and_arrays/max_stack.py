class ListNode(int):
    def __init__(self, val):
        self.val = val
        self.next = None
        self.isDeleted = False


class Cmp(ListNode):
    def __init__(self, item):
        self.item = item

    def __lt__(self, other):
        return self.item < other.iter


class MaxStack:

    def __init__(self):
        self.stack = None
        self.heap = []

    def push(self, x: int) -> None:
        item = ListNode(x)
        heappush(self.heap, item, key=Cmp)
        item.next, self.stack = self.stack, item

    def pop(self) -> int:
        node = self.stack
        while node:
            if node.isDeleted == False:
                self.stack = node.next
                node.isDeleted = True
                return node.val
            node = node.next

    def top(self) -> int:
        node = self.stack
        while node:
            if node.isDeleted == False:
                self.stack = node
                return node.val
            node = node.next

    def peekMax(self) -> int:
        while self.heap:
            if self.heap[0].isDelete == True:
                heappop(self.heap)
            else:
                return self.heap[0]

    def popMax(self) -> int:
        while self.heap:
            item = heappop(self.heap)
            if item.isDeleted == False:
                item.isDeleted = True
                return item.val

        # O(lgn)


def max_heap(A, parent, heapsize, key=None):
    cmp_func = lambda item: item if key is None else key
    l = 2 * parent + 1
    r = 2 * parent + 2
    largest = parent
    if l <= heapsize and cmp_func(A[l]) > cmp_func(A[parent]):
        largest = l
    if r <= heapsize and cmp_func(A[r]) > cmp_func(A[largest]):
        largest = r
    if largest != parent:
        A[parent], A[largest] = A[largest], A[parent]
        max_heap(A, largest, heapsize)
    # O(n)

def heappop(heap):
    """Pop the smallest item off the heap, maintaining the heap invariant."""
    lastelt = heap.pop()    # raises appropriate IndexError if heap is empty
    if heap:
        returnitem = heap[0]
        heap[0] = lastelt
        _siftup(heap, 0)
        return returnitem
    return lastelt

def _siftup(heap, pos):
    endpos = len(heap)
    startpos = pos
    newitem = heap[pos]
    # Bubble up the smaller child until hitting a leaf.
    childpos = 2*pos + 1    # leftmost child position
    while childpos < endpos:
        # Set childpos to index of smaller child.
        rightpos = childpos + 1
        if rightpos < endpos and not heap[childpos] > heap[rightpos]:
            childpos = rightpos
        # Move the smaller child up.
        heap[pos] = heap[childpos]
        pos = childpos
        childpos = 2*pos + 1
    # The leaf at pos is empty now.  Put newitem there, and bubble it up
    # to its final resting place (by sifting its parents down).
    heap[pos] = newitem
    __siftdown(heap, startpos, pos)

def pop_max(A):
    lastelt = A.pop()
    if A:
        returnitem = A[0]
        A[0] = lastelt
        max_heap(A, 0, len(A) - 1)
        return returnitem
    return lastelt


def heappush(heap, item, key):
    heap.append(item)
    __siftdown(heap, 0, len(heap) - 1, key)


def __siftdown(heap, startpos, pos, key):
    newitem = heap[pos]
    # Follow the path to the root, moving parents down until finding a place
    # newitem fits.
    while pos > startpos:
        parentpos = (pos - 1) >> 1
        parent = heap[parentpos]
        if key(newitem.val) > key(parent.val):
            heap[pos] = parent
            pos = parentpos
            continue
        break
    heap[pos] = newitem

class MaxStackShort(list):

    def push(self, x: int) -> None:
        # each item we push onto stack goes with the max value on that moment of time
        # we compare max value from the latest value of stack and incoming value
        m = max(x, self[-1][1] if self else float('-inf'))
        self.append((x, m))

    def pop(self) -> int:
        # under index 0 we store value of the stack
        return list.pop(self)[0]

    def top(self) -> int:
        # under index 0 we store value of the stack
        return self[-1][0]

    def peekMax(self) -> int:
        # under index 1 we store max value of the stack
        return self[-1][1]

    def popMax(self) -> int:
        # we note current
        m = self[-1][1]
        b = []
        # since we need to pop max we need to find the element that equals to the current max
        # let say we have this [(6,6),(1,6),(5,5),(2,5),(4,5)]
        while self[-1][0] != m:
            b.append(self.pop())
        # b will contain [(2,5),(4,5)]

        self.pop() # here (5,5) will be popped out
        # now self is [(5,5),(1,5)]
        for item in reversed(b):
            self.push(item)
        # after pushing from b self is
        # [(6,6), (1,6), (2,6), (4,6)]
        # NOTE: this does not work
        #map(self.push, reversed(b))
        return m

if __name__ == "__main__":
    s = MaxStackShort()
    # s.push(5)
    # s.push(1)
    # s.push(5)
    # print(s.top()) #5
    # print(s.popMax()) #5
    # print(s.top()) # 1
    # print(s.peekMax())
    # print(s.pop())
    # print(s.top())
    s.push(5)
    s.push(1)
    s.popMax()
    s.peekMax()

    oper = ["MaxStack", "push", "top", "push", "peekMax", "pop", "top", "push", "top", "push", "pop", "peekMax", "pop", "top",
     "popMax", "push", "push", "top", "push", "popMax", "top", "push", "pop", "push", "pop", "push", "top", "top",
     "popMax", "top", "push", "peekMax", "peekMax", "top", "push", "push", "peekMax", "popMax", "peekMax", "pop",
     "popMax", "popMax", "popMax", "push", "peekMax", "pop", "push", "push", "top", "push", "peekMax", "push", "pop",
     "pop", "pop", "popMax", "push", "peekMax", "push", "push", "top", "push", "pop", "popMax", "push", "push", "pop",
     "push", "peekMax", "peekMax", "top", "push", "push", "push", "push", "pop", "top", "top", "popMax", "push",
     "peekMax", "push", "push", "pop", "peekMax", "push", "push", "pop", "push", "top", "peekMax", "popMax", "push",
     "push", "push", "top", "top", "pop", "push", "top", "pop", "peekMax", "push", "popMax", "top", "push", "top",
     "push", "push", "top", "push", "push", "top", "pop", "push", "peekMax", "pop", "peekMax", "top", "peekMax", "push",
     "push", "peekMax", "top", "push", "push", "top", "popMax", "peekMax", "top", "popMax", "push", "push", "popMax",
     "pop", "peekMax", "popMax", "top", "push", "top", "top", "popMax", "top", "pop", "top", "pop", "push", "popMax",
     "peekMax", "top", "pop", "push", "push", "peekMax", "push", "pop", "push", "push", "popMax", "push", "push", "top",
     "peekMax", "popMax", "peekMax", "push", "peekMax", "push", "push", "peekMax", "push", "peekMax", "top", "top",
     "popMax", "push", "push", "pop", "push", "top", "push", "peekMax", "peekMax", "push", "peekMax", "push", "peekMax",
     "popMax", "push", "push", "push", "popMax", "top", "top", "push", "push", "push", "popMax", "popMax", "push",
     "push", "peekMax", "push", "top", "push", "popMax", "peekMax", "pop", "peekMax", "push", "push", "peekMax", "pop",
     "push", "push", "peekMax", "push", "peekMax", "pop", "push", "push", "top", "top", "push", "top", "push", "top",
     "push", "push", "peekMax", "push", "top", "top", "popMax", "peekMax", "push", "popMax", "top", "push", "peekMax",
     "pop", "push", "push", "push", "popMax", "top", "peekMax", "top", "popMax", "popMax", "peekMax", "peekMax", "push",
     "push", "push", "popMax", "push", "pop", "top", "popMax", "peekMax", "peekMax", "peekMax", "push", "top", "top",
     "peekMax", "peekMax", "push", "popMax", "peekMax", "push", "pop", "push", "popMax", "push", "top", "push",
     "popMax", "popMax", "pop", "peekMax", "top", "top", "pop", "peekMax", "push", "pop", "popMax", "push", "pop",
     "push", "peekMax", "pop", "top", "pop", "peekMax", "peekMax", "push", "popMax", "top", "top", "push", "push",
     "popMax", "push", "popMax", "push", "push", "top", "pop", "push", "popMax", "push", "push", "top", "top", "top",
     "push", "top", "push", "top", "peekMax", "push", "pop", "pop", "popMax", "push", "push", "pop", "push", "push",
     "popMax", "pop", "pop", "top", "peekMax", "push", "push", "pop", "push", "push", "peekMax", "pop", "pop", "top",
     "peekMax", "pop", "push", "top", "push", "peekMax", "push", "pop", "push", "top", "top", "top", "push", "popMax",
     "push", "pop", "push", "popMax", "push", "pop", "pop", "peekMax", "top", "push", "peekMax", "top", "peekMax",
     "top", "push", "push", "push", "top", "peekMax", "pop", "push", "pop", "popMax", "pop", "push", "popMax", "pop",
     "pop", "peekMax", "push", "push", "peekMax", "popMax", "push", "peekMax", "pop", "push", "push", "peekMax", "top",
     "push", "push", "popMax", "push", "popMax", "push", "push", "peekMax", "peekMax", "push", "peekMax", "pop", "push",
     "peekMax", "push", "peekMax", "push", "push", "push", "popMax", "pop", "push", "pop", "pop", "push", "push", "top",
     "popMax", "pop", "popMax", "popMax", "pop", "popMax", "peekMax", "top", "peekMax", "popMax", "top", "top",
     "peekMax", "push", "push", "popMax", "push", "top", "top", "top", "top", "push", "push", "top", "push", "push",
     "peekMax", "push", "push", "push", "popMax", "push", "pop", "push", "push", "peekMax", "top", "push", "top", "pop",
     "top", "push", "popMax", "push", "top", "popMax", "peekMax", "push", "push", "peekMax", "popMax", "popMax", "push",
     "pop", "top", "top", "pop", "top", "push", "popMax", "top", "peekMax", "push", "push", "top", "push", "pop",
     "push", "peekMax", "peekMax", "peekMax", "push", "pop", "top", "pop", "push", "popMax", "push", "pop", "top",
     "push", "push", "pop", "peekMax", "peekMax", "pop", "push", "push", "push", "pop", "popMax", "pop", "peekMax",
     "push", "popMax", "peekMax", "top", "peekMax", "push", "pop", "pop", "pop", "push", "peekMax", "pop", "top",
     "popMax", "push", "popMax", "popMax", "top", "push", "peekMax", "popMax", "peekMax", "push", "push", "push", "pop",
     "push", "push", "peekMax", "push", "top", "pop", "push", "pop", "pop", "pop", "top", "push", "top", "peekMax",
     "popMax", "pop", "top", "push", "push", "peekMax", "popMax", "popMax", "push", "pop", "push", "pop", "push",
     "push", "push", "top", "peekMax", "popMax", "peekMax", "push", "push", "push", "pop", "push", "push", "top",
     "push", "peekMax", "popMax", "top", "push", "push", "push", "push", "top", "push", "pop", "top", "pop", "push",
     "top", "top", "top", "top", "push", "peekMax", "push", "popMax", "popMax", "top", "push", "peekMax", "popMax",
     "popMax", "push", "push", "popMax", "pop", "push", "push", "top", "popMax", "popMax", "push", "popMax", "push",
     "popMax", "peekMax", "popMax", "popMax", "push", "peekMax", "push", "push", "top", "top", "popMax", "push", "push",
     "top", "push", "peekMax", "push", "popMax", "push", "top", "top", "pop", "popMax", "top", "top", "push", "pop",
     "popMax", "peekMax", "popMax", "popMax", "peekMax", "top", "push", "push", "push", "popMax", "peekMax", "popMax",
     "push", "pop", "pop", "pop", "push", "push", "push", "pop", "popMax", "push", "push", "push", "pop", "push",
     "popMax", "popMax", "top", "top", "pop", "popMax", "pop", "push", "peekMax", "push", "push", "popMax", "popMax",
     "peekMax", "popMax", "push", "push", "top", "pop", "pop", "top", "pop", "top", "pop", "top", "push", "push", "pop",
     "push", "top", "push", "push", "top", "top", "pop", "push", "top", "top", "top", "push", "top", "popMax", "push",
     "peekMax", "push", "pop", "popMax", "peekMax", "top", "peekMax", "popMax", "top", "push", "popMax", "push", "push",
     "peekMax", "popMax", "popMax", "push", "peekMax", "peekMax", "peekMax", "push", "push", "top", "push", "push",
     "push", "push", "peekMax", "popMax", "peekMax", "pop", "push", "push", "top", "peekMax", "push", "popMax",
     "peekMax"]
    data = [[], [-9], [], [81], [], [], [], [-91], [], [22], [], [], [], [], [], [-66], [89], [], [97], [], [], [5], [], [24],
     [], [21], [], [], [], [], [-12], [], [], [], [-47], [-46], [], [], [], [], [], [], [], [47], [], [], [82], [-36],
     [], [-29], [], [73], [], [], [], [], [-2], [], [5], [72], [], [-6], [], [], [-78], [-6], [], [-22], [], [], [],
     [-85], [89], [-11], [-5], [], [], [], [], [-93], [], [9], [-91], [], [], [-89], [43], [], [9], [], [], [], [-86],
     [-41], [-86], [], [], [], [-9], [], [], [], [-61], [], [], [23], [], [-84], [-89], [], [42], [-31], [], [], [18],
     [], [], [], [], [], [-34], [71], [], [], [52], [-74], [], [], [], [], [], [99], [18], [], [], [], [], [], [-20],
     [], [], [], [], [], [], [], [-23], [], [], [], [], [82], [8], [], [-74], [], [81], [90], [], [13], [-74], [], [],
     [], [], [-30], [], [69], [17], [], [-39], [], [], [], [], [-6], [-56], [], [74], [], [61], [], [], [48], [], [41],
     [], [], [13], [-88], [87], [], [], [], [-1], [-34], [72], [], [], [40], [-37], [], [59], [], [60], [], [], [], [],
     [73], [-42], [], [], [-29], [99], [], [-62], [], [], [55], [91], [], [], [94], [], [-3], [], [97], [40], [], [-25],
     [], [], [], [], [88], [], [], [-17], [], [], [74], [-65], [79], [], [], [], [], [], [], [], [], [85], [42], [49],
     [], [25], [], [], [], [], [], [], [-76], [], [], [], [], [35], [], [], [-8], [], [80], [], [79], [], [29], [], [],
     [], [], [], [], [], [], [46], [], [], [81], [], [41], [], [], [], [], [], [], [14], [], [], [], [-54], [-3], [],
     [-33], [], [-14], [15], [], [], [-38], [], [-52], [58], [], [], [], [18], [], [41], [], [], [-62], [], [], [],
     [-35], [-16], [], [70], [-79], [], [], [], [], [], [-48], [-48], [], [62], [-11], [], [], [], [], [], [], [-60],
     [], [-43], [], [-98], [], [100], [], [], [], [99], [], [77], [], [10], [], [-58], [], [], [], [], [-81], [], [],
     [], [], [83], [80], [-85], [], [], [], [-82], [], [], [], [7], [], [], [], [], [-85], [28], [], [], [-96], [], [],
     [58], [16], [], [], [-61], [-70], [], [-8], [], [-84], [89], [], [], [85], [], [], [-39], [], [-100], [], [21],
     [58], [12], [], [], [-10], [], [], [-69], [52], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [-82],
     [32], [], [78], [], [], [], [], [-15], [-11], [], [-61], [-38], [], [-84], [-44], [-45], [], [-12], [], [-97],
     [-54], [], [], [-79], [], [], [], [26], [], [-2], [], [], [], [-47], [-59], [], [], [], [-53], [], [], [], [], [],
     [29], [], [], [], [57], [-80], [], [-97], [], [-32], [], [], [], [-63], [], [], [], [43], [], [50], [], [], [60],
     [79], [], [], [], [], [-82], [94], [-10], [], [], [], [], [-48], [], [], [], [], [96], [], [], [], [-44], [], [],
     [], [], [-45], [], [], [], [47], [], [], [], [79], [74], [-44], [], [-60], [-83], [], [-4], [], [], [-25], [], [],
     [], [], [-98], [], [], [], [], [], [80], [-43], [], [], [], [66], [], [75], [], [10], [63], [67], [], [], [], [],
     [61], [5], [55], [], [68], [-35], [], [-93], [], [], [], [41], [-99], [-1], [-100], [], [-26], [], [], [], [-73],
     [], [], [], [], [81], [], [-22], [], [], [], [-62], [], [], [], [-30], [-84], [], [], [-24], [-9], [], [], [],
     [67], [], [-89], [], [], [], [], [-28], [], [-71], [-53], [], [], [], [32], [-44], [], [-29], [], [91], [], [-1],
     [], [], [], [], [], [], [-88], [], [], [], [], [], [], [], [-81], [-91], [-1], [], [], [], [-14], [], [], [],
     [-98], [-89], [-25], [], [], [98], [-24], [61], [], [0], [], [], [], [], [], [], [], [60], [], [-62], [-20], [],
     [], [], [], [59], [76], [], [], [], [], [], [], [], [], [-100], [-39], [], [59], [], [92], [1], [], [], [], [30],
     [], [], [], [-50], [], [], [-38], [], [-71], [], [], [], [], [], [], [], [-58], [], [9], [33], [], [], [], [27],
     [], [], [], [-17], [43], [], [92], [-25], [-61], [83], [], [], [], [], [-84], [36], [], [], [-69], [], []]

    for i, o in enumerate(oper):
        if o == "MaxStack":
            continue
        elif o == "push":
            s.push(data[i][0])
        elif o == "top":
            print(s.top())
        elif o == "peekMax":
            print(s.peekMax())
        elif o == "popMax":
            print(s.popMax())
        elif o == "pop":
            print(s.pop())

import heapq





