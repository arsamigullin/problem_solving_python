def solution(A):
    # write your code in Python 3.6
    d = dict()
    for i in range(0, len(A)):
        if A[i] in d:
            d[A[i]] += 1
        else:
            d[A[i]] = 1
    for k, v in d.items():
        if v % 2 == 1:
            return k

    return -1
