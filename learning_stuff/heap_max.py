# O(lgn)
def max_heap(A, parent, heapsize, key=None):
    cmp_func = lambda item: item if key is None else key
    l = 2 * parent + 1
    r = 2 * parent + 2
    largest = parent
    if l <= heapsize and cmp_func(A[l])>cmp_func(A[parent]):
        largest = l
    if r <= heapsize and cmp_func(A[r]) > cmp_func(A[largest]):
        largest = r
    if largest!=parent:
        A[parent], A[largest] = A[largest], A[parent]
        max_heap(A, largest, heapsize)
# O(n)
def heapify(A, key=None):
    if not A:
        raise ValueError("input array must not be empty")
    heapsize = len(A) - 1
    for i in range(len(A)//2, -1, -1):
        max_heap(A, i, heapsize, key=None)

def pop_max(A):
    lastelt = A.pop()
    if A:
        returnitem = A[0]
        A[0] = lastelt
        max_heap(A,0,len(A)-1)
        return returnitem
    return lastelt

# O(nlgn)
def heapsort(A, key=None):
    heapsize = len(A)-1
    heapify(A, key)
    for i in range(len(A) - 1, -1, -1):
        A[0], A[i] = A[i], A[0]
        heapsize -= 1
        max_heap(A, 0, heapsize, key)

def heappush(heap, item):
    """Push item onto heap, maintaining the heap invariant."""
    heap.append(item)
    __siftdown(heap, 0, len(heap)-1)


def __siftdown(heap, startpos, pos):
    newitem = heap[pos]
    # Follow the path to the root, moving parents down until finding a place
    # newitem fits.
    while pos > startpos:
        parentpos = (pos - 1) >> 1
        parent = heap[parentpos]
        if newitem > parent:
            heap[pos] = parent
            pos = parentpos
            continue
        break
    heap[pos] = newitem


if __name__ == "__main__":
    heap = []
    for n in [1,5,2,8,10,3]:
        heappush(heap,n)

    while heap:
        print(pop_max(heap))


    import heapq
    a = [3,1,8,6]
    b = [3,1,8,6]
    heapq.heapify(a)
    heapq.heappush(a, -1)
    popped = heapq.heappop(a)
    heapify(b)
    heappush(b, -1)
    popped = pop_max(b)
    heapsort(b)
    print(a, b)

