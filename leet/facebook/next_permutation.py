#1.Start from the end and find the first item in decreasing order, for example
#   4, 9, 5, 3, 1. Starting from 1 to 9 is increasing order. 4 is the first item in decr order.
#   if all the nums in increasing order just reverse them
#2. Find first element that is large than 4 starting from the end
#3. Swap those two element
#4. Reverse elements between i and len(nums)

def nextPermutation(nums):
    """
    :type nums: List[int]
    :rtype: None Do not return anything, modify nums in-place instead.
    """
    #1
    i = len(nums) - 2
    while i >= 0 and nums[i] >= nums[i + 1]:
        i -= 1

    if i < 0:
        nums.reverse()
        return
    #2
    j = len(nums) - 1
    while j >= 0 and nums[j] <= nums[i]:
        j -= 1

    #3
    nums[i], nums[j] = nums[j], nums[i]

    #4
    start = i + 1
    end = len(nums) - 1

    while start < end:
        nums[start], nums[end] = nums[end], nums[start]
        start += 1
        end -= 1

if __name__ == "__main__":
    nextPermutation([5, 1, 1])
    nextPermutation([4,9,5])