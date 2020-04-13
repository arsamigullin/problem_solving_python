
# this problem
# https://leetcode.com/problems/wiggle-sort/submissions/


import typing
List = typing.List


class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        is_mid_max = True
        
        for i in range(len(nums)-1):
            if is_mid_max:
                if nums[i] > nums[i+1]:
                    nums[i], nums[i+1] = nums[i+1], nums[i]
                            
            else:
                if nums[i] < nums[i+1]:
                    nums[i], nums[i+1] = nums[i+1], nums[i]
            
            is_mid_max ^= 1



if __name__ == "__main__":
    s = Solution()
    s.wiggleSort([3,5,2,1,6,4])

def quicksortasc(A, s, e):
    if s<e:
        q = partitionasc(A, s, e)
        quicksortasc(A, s, q-1)
        quicksortasc(A, q+1, e)


def partitionasc(A,s,e):
    x = A[e] #  pivot element around which to partition the subarray
    i = s - 1 # start element, it can be negative
    for j in range(s, e):
        # once the current element is less or equal pivot
        # we swap values between i and j indexes
        # so under i index we have value that less or equal than pivot
        # i is just pointing where we will insert the current item that is less or equal pivot
        if A[j] <= x:
            i+=1
            A[j], A[i] = A[i], A[j]
    A[i+1], A[e] = A[e], A[i+1]
    return i+1