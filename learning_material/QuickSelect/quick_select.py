import random


def rand_partition(A, l, r):
    p = random.randint(l, r)
    A[l], A[p] = A[p], A[l]
    p = A[l]
    m = l
    for k in range(l + 1, r + 1):
        if A[k] < p:
            m+=1
            A[k], A[m] = A[m], A[k]
    A[l], A[m] = A[m], A[l]
    return m

def quick_select(A, l, r, k):
    if l == r:
        return A[l]
    q = rand_partition(A, l, r)
    if q + 1 == k:
        print(A[:q + 1])
        return A[q]
    elif q + 1 > k:
        return quick_select(A, l, q - 1, k)
    else:
        # if we need all items less than k, then we do this
        # result.append(A[q])

        return quick_select(A, q + 1, r, k)

if __name__ == '__main__':
    A = [3,2,1]
    rand_partition(A,0,2)
    A = [2, 8, 7, 1, 5, 4, 6, 3]
    print(quick_select(A, 0, 7, 4))