from typing import List
# As we know Knuth's permutation is searches for the next permutation in lexicographically order
# so we cannot use it here as it is because we need to find
# "lexicographically largest permutation that is smaller than arr"

# but we can slightly modify Knuth's permutation
# basically the problem is to find the previous permutation
class Solution:
    def prevPermOpt1(self, arr: List[int]) -> List[int]:

        # to find the next permutation we would search the first item that is less than the previous one
        # to find the previous permutation we search the first item that is greater the or eq than the previous one
        # if arr = [1,4,3,5,7] then after this loop i = 1
        i = len(arr) - 2
        while i >= 0 and arr[i] <= arr[i + 1]:
            i -= 1


        if i < 0:
            return arr

        # in the next permutation we would then find the first item that is largest than current one
        # in the previous permutation we find the first item that is less than current one
        # arr = [1,4,3,5,7] i=1, the first smallest than arr[i] is 3
        j = len(arr) - 1
        while j > i and (arr[i] <= arr[j] or arr[j - 1] == arr[j]):
            j -= 1

        # here just swap them
        # result [1,3,4,5,7]
        arr[i], arr[j] = arr[j], arr[i]
        return arr




if __name__ == "__main__":
    arr = [3,2,1]
    arr = [1,1,5]
    arr = [3,1,1,3]
    s = Solution()
    s.prevPermOpt1(arr)
