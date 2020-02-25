def max_heap(A, parent, heapsize, key=None):
    cmp_func = lambda item: item if key is None else key
    l = 2 * parent + 1
    r = 2 * parent + 2
    smallest = parent
    if l <= heapsize and cmp_func(A[l]) < cmp_func(A[parent]):
        smallest = l
    if r <= heapsize and cmp_func(A[r]) < cmp_func(A[smallest]):
        smallest = r
    if smallest!=parent:
        A[parent], A[smallest] = A[smallest], A[parent]
        max_heap(A, smallest, heapsize)

def heapify(A, key=None):
    if not A:
        raise ValueError("input array must not be empty")
    heapsize = len(A) - 1
    for i in range(len(A)//2, -1, -1):
        max_heap(A, i, heapsize, key=None)

def heapsort(A, key=None):
    heapsize = len(A)-1
    heapify(A, key)
    for i in range(len(A) - 1, -1, -1):
        A[0], A[i] = A[i], A[0]
        heapsize -= 1
        max_heap(A, 0, heapsize, key)


if __name__ == "__main__":
    import heapq
    a = [3,1,8,6]
    b = [3,1,8,6]
    heapq.heapify(a)
    heapify(b)
    heapsort(b)
    print(a, b)
