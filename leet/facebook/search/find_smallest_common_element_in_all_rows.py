# https://leetcode.com/problems/find-smallest-common-element-in-all-rows/submissions/

# We need to find the smalles common to each array item
# we take the first array and do binary search in each array of each item from the first array
# since items in sorted order the first found common item will be the minimal

import typing
List = typing.List

class Solution:
    def smallestCommonElement(self, mat: List[List[int]]) -> int:
        if len(mat) == 1:
            return mat[0][0]
        def binary_search(arr, target):
            s = 0
            e = len(arr) - 1
            while s <= e:
                #mid = s+(e-s)//2 #this works as well as the command right below
                mid = e - (e-s)//2
                if arr[mid] == target:
                    return True
                elif arr[mid] > target:
                    e = mid - 1
                else:
                    s = mid + 1
            return False
        for t in mat[0]:
            is_common = True
            for i in range(1,len(mat)):
                if not binary_search(mat[i],t):
                    is_common = False
                    break
            if is_common:
                return t
        return -1
if __name__ == "__main__":
    s = Solution()
    s.smallestCommonElement([[1,2,3],[2,3,4],[2,3,5]])
    #s.smallestCommonElement([[1,2,3,4,5],[2,4,5,8,10],[3,5,7,9,11],[1,3,5,7,9]])
