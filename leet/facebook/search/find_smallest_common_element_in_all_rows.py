import typing
List = typing.List

class Solution:
    def smallestCommonElement(self, mat: List[List[int]]) -> int:
        if len(mat) == 1:
            return mat[0][0]
        def binary_search(arr, target):
            s = 0
            e = len(arr) - 1
            while s < e:
                mid = e-(e-s)//2
                if arr[mid] == target:
                    return True
                elif arr[mid] > target:
                    e = mid - 1
                elif arr[mid] < target:
                    s = mid + 1
            return False
        for target in mat[0]:
            is_common = True
            for i in range(1,len(mat)):
                if not binary_search(mat[i],target):
                    is_common = False
                    break
            if is_common:
                return target
        return -1
if __name__ == "__main__":
    s = Solution()
    s.smallestCommonElement([[1,2,3],[2,3,4],[2,3,5]])
    #s.smallestCommonElement([[1,2,3,4,5],[2,4,5,8,10],[3,5,7,9,11],[1,3,5,7,9]])
