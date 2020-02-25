class Heap:
    def __init__(self, A):
        self.length = len(A)
        # heapsize points to the latest element of the heap
        self.heapsize = len(A) - 1
        self.A = A

    def left(self,i):
        return 2*i+1

    def right(self, i):
        return 2*i+2

    def parent(self,i):
        return i//2
    # lg(n)
    def max_hepify(self,i):
        # i is parent
        # l and r its children
        l = self.left(i)
        r = self.right(i)
        # here we determine the largest element between parent and l
        if l <= self.heapsize and self.A[l] > self.A[i]:
            largest = l
        else:
            largest = i
        # here we determine largest element between largest (that was determined above) and right
        if r <= self.heapsize and self.A[r] > self.A[largest]:
            largest = r
        # here we swap the largest element and parent so the parent element becomes larger
        if largest!=i:
            self.A[i], self.A[largest] = self.A[largest], self.A[i]
            # we do the same procedure with
            self.max_hepify(largest)
    #O(n)
    def build_max_heap(self):
        for i in range(len(self.A)//2, -1, -1):
            self.max_hepify(i)
        print('done')

    def heap_extrac_max(self):
        if self.heapsize < 0:
            raise LookupError('head is empty')


    def heapsort(self):
        # O(nlgn)
        self.build_max_heap()
        #O(nlgn)
        for i in range(len(self.A)-1, 0, -1):
            # at this time we have largest element at index 0
            #
            self.A[0], self.A[i] = self.A[i], self.A[0]

            self.heapsize-=1
            self.max_hepify(0)
        print('done')


# Python program for implementation of heap Sort

# To heapify subtree rooted at index i.
# n is size of heap
def heapify(arr, n, i):
    largest = i  # Initialize largest as root
    l = 2 * i + 1  # left = 2*i + 1
    r = 2 * i + 2  # right = 2*i + 2

    # See if left child of root exists and is
    # greater than root
    if l < n and arr[i] < arr[l]:
        largest = l

        # See if right child of root exists and is
    # greater than root
    if r < n and arr[largest] < arr[r]:
        largest = r

        # Change root, if needed
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # swap

        # Heapify the root.
        heapify(arr, n, largest)

    # The main function to sort an array of given size


def heapSort(arr):
    n = len(arr)

    # Build a maxheap.
    for i in range(n//2, -1, -1):
        heapify(arr, n, i)
    print(arr)

        # One by one extract elements
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # swap
        heapify(arr, i, 0)


if __name__ == "__main__":
    #a = [4,1,3,2,16,9,10,14,8,7]
    #heapSort(a)
    #s = Heap([4,1,3,2,16,9,10,14,8,7])
    s = Heap([8,6,4,3])
    s.build_max_heap()
    s.heapsort()
    print('done')
