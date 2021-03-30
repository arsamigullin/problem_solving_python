from typing import List


class Solution:
    def advantageCount(self, A: List[int], B: List[int]) -> List[int]:
        indexedB = [(v, i) for i, v in enumerate(B)]
        A.sort()
        indexedB.sort()
        res = [0] * len(A)
        i=0
        for a in A:
            b, ind = indexedB[i]
            # a beats b
            if a>b:
                # add a
                res[ind] = a
                # go to the next b
                i+=1
            else:
                # a does not beat b
                # we want to add the largest b
                _, ind =indexedB.pop()
                res[ind] = a
        return res

if __name__ == '__main__':
    s = Solution()
    s.advantageCount([2,7,11,15], [1,10,4,11])