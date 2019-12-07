import collections
# brute force
def lenLongestFibSubseq(A):
    n = len(A)
    ans = 0
    S = set(A)
    for i in range(0, n):
        for j in range(i+1, n):
            # note, x is not A[0] but A[1]
            x, y = A[j], A[i] + A[j]
            l = 0
            while y in S:
                l+=1
                x, y = y, x + y
            ans = max(ans, l)

    return 0 if n<3 else ans

import collections
# this is my own implementation to memorize it
def lenLongestFibSubseqDp1(A):
    # dict where keys are values.
    val_index_dict = {val: i for i, val in enumerate(A)}
    # storage for length
    pair_dict = collections.defaultdict(lambda : 2)
    ans = 0
    # i, j, k
    # this is what actually happens
    # since A[i] + A[j] = A[k], hence A[k] - A[j] = A[i]
    for k, val in enumerate(A):
        for j in range(k):
            i = val_index_dict.get(val - A[j])
            if i is not None and i < j:
                pair_dict[j, k] = pair_dict[i, j] + 1
                ans = max(pair_dict[j, k], ans)
    return ans if ans>=3 else 0


if __name__ == "__main__":
    lenLongestFibSubseqDp1([1,2,3,4,5,6,7,8])
    lenLongestFibSubseq([1,2,3,4,5,6,7,8])
