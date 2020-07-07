from typing import List


class Solution:
    def minDominoRotations(self, A: List[int], B: List[int]) -> int:
        numsA = set(A)
        numsB = set(B)

        def helper(numset, nums1, nums2):
            tot = float('inf')
            for num in numset:
                cnt = 0
                for i in range(len(nums1)):
                    if nums1[i] != num:
                        if nums2[i] == num:
                            cnt += 1
                        else:
                            cnt = float('inf')
                            break
                tot = min(tot, cnt)

            return -1 if tot == float('inf') else tot

        resA = helper([A[0], B[0]], A, B)
        resB = helper([A[0], B[0]], B, A)
        # this is also working
        #resA = helper(numsA, A, B)
        #resB = helper(numsB, B, A)
        if resA == -1 and resB == -1:
            return -1
        elif resA > -1 and resB > -1:
            return min(resA, resB)
        else:
            return max(resA, resB)


class Solution:
    def minDominoRotations(self, A: List[int], B: List[int]) -> int:
        for x in [A[0], B[0]]:
            if all(x in d for d in zip(A,B)):
                return len(A) - max(A.count(x), B.count(x))
        return -1


class Solution:
    def minDominoRotations(self, A: List[int], B: List[int]) -> int:
        def check(x):
            """
            Return min number of swaps
            if one could make all elements in A or B equal to x.
            Else return -1.
            """
            # how many rotations should be done
            # to have all elements in A equal to x
            # and to have all elements in B equal to x
            rotations_a = rotations_b = 0
            for i in range(n):
                # rotations coudn't be done
                if A[i] != x and B[i] != x:
                    return -1
                # A[i] != x and B[i] == x
                elif A[i] != x:
                    rotations_a += 1
                # A[i] == x and B[i] != x
                elif B[i] != x:
                    rotations_b += 1
            # min number of rotations to have all
            # elements equal to x in A or B
            return min(rotations_a, rotations_b)

        n = len(A)
        rotations = check(A[0])
        # If one could make all elements in A or B equal to A[0]
        if rotations != -1 or A[0] == B[0]:
            return rotations
            # If one could make all elements in A or B equal to B[0]
        else:
            return check(B[0])