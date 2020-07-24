from typing import List
# As we know Knuth's permutation is searches for the next permutation in lexicographically order
# so we cannot use it here as it is because we need to find
# "lexicographically largest permutation that is smaller than arr"

# but we can slightly modify Knuth's permutation

class Solution:
    def prevPermOpt1(self, arr: List[int]) -> List[int]:

        i = len(arr) - 2
        while i >= 0 and arr[i] <= arr[i + 1]:
            i -= 1

        if i < 0:
            return arr

        j = len(arr) - 1
        while j > i and (arr[i] <= arr[j] or arr[j - 1] == arr[j]):
            j -= 1

        arr[i], arr[j] = arr[j], arr[i]
        return arr




if __name__ == "__main__":
    arr = [3,2,1]
    arr = [1,1,5]
    arr = [3,1,1,3]
    s = Solution()
    s.prevPermOpt1(arr)
