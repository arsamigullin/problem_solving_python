def quicksort(A, s, e):
    if s<e:
        q = partitionasc(A, s, e)
        quicksort(A, s, q-1)
        quicksort(A, q+1, e)


def partitionasc(A,s,e):
    x = A[e] #  pivot element around which to partition the subarray
    i = s - 1 # start element, it can be negative
    for j in range(s, e):
        # once the current element is less or equal pivot
        # we swap values between i and j indexes
        # so under i index we have value that less or equal than pivot
        # i is just pointing to where we will insert the current item that is less or equal pivot
        if A[j] <= x:
            i+=1
            A[j], A[i] = A[i], A[j]
    A[i+1], A[e] = A[e], A[i+1]
    return i+1

if __name__ == "__main__":
    A = [2,8,7,1,3,6,4]
    quicksort(A, 0, len(A)-1)
    print(A)