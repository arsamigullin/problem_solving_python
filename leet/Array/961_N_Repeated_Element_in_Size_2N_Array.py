import collections


class Solution(object):
    def repeatedNTimes(self, A):
        count = collections.Counter(A)
        for k in count:
            if count[k] > 1:
                return k


class Solution(object):
    def repeatedNTimes(self, A):
        for k in range(1, 4):
            for i in range(len(A) - k):
                if A[i] == A[i+k]:
                    return A[i]


class Solution(object):
    def repeatedNTimes(self, A):
        uniq = set()
        for a in A:
            if a not in uniq:
                uniq.add(a)
            else:
                return a