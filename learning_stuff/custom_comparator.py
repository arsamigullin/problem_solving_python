class SomeObj(int):
    def __init__(self, x):
        self.x = x

class Cmp(SomeObj):
    def __init__(self, item):
        self.x = item

    def __le__(self, other):
        return self.x <= other.x

    def __ge__(self, other):
        return self.x >= other.x


def quicksort(A, key=None):
    __quicksort(A, 0, len(A) - 1, key)

def __quicksort(A, s, e, key=None):
    if s<e:
        q = partition(A, s, e, key)
        __quicksort(A, s, q - 1, key)
        __quicksort(A, q + 1, e, key)

def partition(A,s,e,key=None):
    pivot = A[e]
    i = s - 1
    for j in range(s, e):
        if key is None:
            if A[j] >= pivot:
                i+=1
                A[j], A[i] = A[i], A[j]
        else:
            if key(A[j]) >= key(pivot):
                i+=1
                A[j], A[i] = A[i], A[j]
    A[i+1], A[e] = A[e], A[i+1]
    return i + 1


class CmpTup(tuple):
    def __lt__(self, other):
        return self[0] > other[0] and self[1]<other[1]



if __name__ == "__main__":

    tuparr = [(1, 3, 0), (2, 4, 1), (3, 5, 2), (4, 1, 3), (5, 2, 4)]
    tuparr.sort(key=CmpTup)

    A = [SomeObj(2),SomeObj(9),SomeObj(5),SomeObj(38),SomeObj(1)]
    quicksort(A, key=Cmp)
    print(A)
    #arr = [SomeObj(2),SomeObj(9),SomeObj(5),SomeObj(38),SomeObj(1)]
    #arr.sort(key=Cmp)
    #print([item.x for item in arr])

