# Merge two sorted sublists `A[low … mid]` and `A[mid+1 … high]`
def merge(A, aux, low, mid, high):
    k = low
    i = low
    j = mid + 1

    # While there are elements in the left and right runs
    while i <= mid and j <= high:
        if A[i] <= A[j]:
            aux[k] = A[i]
            i+=1
        else:
            aux[k] = A[j]
            j+=1
        k+=1
    # if i exhausted first, then the second part (starting from j to high) is essentially already sorted in aux
    # so the below while will not be executed
    # if j exhausted first, then we must copy the rest elements of the first part to the aux starting from k
    # and this will keeps the aux part (restricted by high) sorted
    while i <= mid:
        aux[k] = A[i]
        k+=1
        i+=1

    # No need to copy the second half (since the remaining items
    # are already in their correct position in the auxiliary array)

    # copy back to the original list to reflect sorted order
    for i in range(low, high + 1):
        A[i] = aux[i]


# Sort list `A[low…high]` using auxiliary list aux
def mergesort(A, aux, low, high):
    # Base case
    if high == low:  # if run size == 1
        return

    # find midpoint
    mid = (low + ((high - low) >> 1))

    # recursively split runs into two halves until run size == 1,
    # then merge them and return up the call chain

    mergesort(A, aux, low, mid)  # split/merge left half
    mergesort(A, aux, mid + 1, high)  # split/merge right half

    merge(A, aux, low, mid, high)  # merge the two half runs


# Function to check if `A` is sorted in ascending order or not
def isSorted(A):
    prev = A[0]
    for i in range(1, len(A)):
        if prev > A[i]:
            print("MergeSort Fails!!")
            return False

        prev = A[i]

    return True

class MergeSortChecking:
    def mergesort(self, A, aux, lo, hi):
        if lo==hi:
            return
        mid = lo + (hi - lo)//2
        self.mergesort(A, aux, lo, mid)
        self.mergesort(A, aux, mid + 1, hi)
        self.merge(A,aux,lo, mid,hi)

    def merge(self,A,aux,lo,mid,hi):
        i = lo
        k = lo
        j = mid+1
        while i<=mid and j<=hi:
            if A[i]<=A[j]:
                aux[k] = A[i]
                i+=1
            else:
                aux[k] = A[j]
                j+=1
            k+=1

        while i <= mid:
            aux[k] = A[i]
            k+=1
            i+=1

        for i in range(lo, hi+1):
            A[i] = aux[i]






# Implementation of merge sort algorithm in Python
if __name__ == '__main__':

    A = [12, 3, 24, 18, 0, 5, -2]
    A = [1,2,3,5,2,3]
    aux = A.copy()
    m = MergeSortChecking()
    m.mergesort(A, aux, 0, len(A)-1)

    print(A)

    # sort list `A` using auxiliary list `aux`
    mergesort(A, aux, 0, len(A) - 1)

    if isSorted(A):
        print(A)
