import bisect

nums = [2,3,4,4,4,7,9]
#nums = [1,2,3,4]
# NOTE: bisect right and bisect left are different only in the >=
#     The return value i is such that all e in a[:i] have e <= x, and all e in
#     a[i:] have e > x.
def bisect_right(x):
    lo = 0
    hi = len(nums)
    while lo < hi:
        mid = (lo + hi) // 2
        if x < nums[mid]:
            hi = mid
        else:
            lo = mid + 1
    return lo

# The return value i is such that all e in a[:i] have e < x, and all e in
#     a[i:] have e >= x
def bisect_left(x):
    lo = 0
    hi = len(nums)
    while lo < hi:
        mid = (lo+hi)//2
        if x <= nums[mid]:
            hi = mid
        else:
            lo = mid + 1
    return lo

# def bisect_left_start(x, start):
#     lo = start
#     hi = len(nums)
#     while lo < hi:
#         mid = (lo+hi)//2
#         if x > nums[mid]:
#             lo = mid+1
#         else:
#             hi = mid
#     return lo



#
# def binary_search_nearest_largest(guess):
#     lo = 0
#     hi = len(nums) - 1
#     res = -1
#     while lo <= hi:
#         mid = (lo + hi) // 2
#         if guess >= nums[mid]:
#             lo = mid + 1
#             res = mid
#         else:
#             hi = mid - 1
#     return res
def binary_search_nearest_largest(guess):
    lo = 0
    hi = len(nums) - 1
    while lo < hi:
        mid = (lo + hi) // 2
        if  guess <= nums[mid]:
            hi = mid
        else:
            lo = mid + 1
    return lo

def binary_search_nearest_smallest(guess):
    lo = 0
    hi = len(nums) - 1
    while lo < hi:
        mid = (lo + hi) // 2
        if guess < nums[mid]:
            hi = mid - 1
        else:
            lo = mid
    return lo

# def binary_search_nearest_smallest(guess):
#     if guess > nums[-1]:
#         return len(nums) - 1
#     lo = 0
#     hi = len(nums) - 1
#     res = -1
#     while lo <= hi:
#         mid = (lo + hi) // 2
#         if guess >= nums[mid]:
#             lo = mid + 1
#             res = mid
#         else:
#             hi = mid - 1
#     return res

# def binary_search_nearest_from_the_right(guess):
#     if guess > nums[-1]:
#         return len(nums) - 1
#     lo = 0
#     hi = len(nums) - 1
#     res = -1
#     while lo <= hi:
#         mid = (lo + hi) // 2
#         if guess >= nums[mid]:
#             lo = mid + 1
#         else:
#             res = mid
#             hi = mid - 1
#     return res

def search(guess):
    lo = 0
    hi = len(nums) - 1
    while lo < hi:
        mid = lo + (hi - lo) // 2
        # if the count of missing numbers before index mid is less than k
        # we want to increase lower
        if guess > nums[mid]:
            lo = mid + 1
        else:
            hi = mid
    return lo

# nearest with bisect
target = 1
insert = bisect.bisect_left(nums, target)
left_nearest = abs(nums[max(insert - 1, 0)])
right_nearest = abs(nums[min(insert, len(nums) - 1)])

def bisect_left_learn(arr, x):
    lo = 0
    hi = len(arr)
    while lo<hi:
        mid = lo + (hi-lo)//2
        if arr[mid] < x:
            lo = mid + 1
        else:
            hi = mid
    return lo

def bisect_right_learn(arr, x):
    lo = 0
    hi = len(arr)
    while lo<hi:
        mid = lo + (hi-lo)//2
        if x < arr[mid]:
            hi = mid
        else:
            lo = mid + 1
    return lo

    # while lo < hi:
    #     mid = (lo+hi)//2
    #     if x < arr[mid]:
    #         hi = mid
    #     else:
    #         lo = mid+1
    # return lo

if __name__ == '__main__':
    # need to find items strictly less than target (or >= target) - use bisect_left
    arr = [10, 20, 30, 40]
    arr = [2,4,5]
    arr = [0]
    arr = [[-1, 0], [0, 5], [1, 6]]
    i = bisect_right_learn(arr, [1])
    i = bisect_left_learn(arr, 3)# arr[:i]<target<=arr[i:]
    # need to find items strictly greater (OR <= target) - use bisect_right
    arr = [5, 20, 30, 40]
    i = bisect_right_learn(arr, 3) # 0
    i = bisect_right_learn(arr, 42) # 4
    i = bisect_right_learn(arr, 5) # 1
    i = bisect_left_learn(arr, 3) # 0
    i = bisect_left_learn(arr, 42) # 4
    i = bisect_left_learn(arr, 5) # 0
    j = bisect.bisect(arr, 5)

    arr = [10,20]
    i = bisect_right_learn(arr, 5) # 0
    i = bisect_right_learn(arr, 10) # 1
    i = bisect_right_learn(arr, 15) # 1
    i = bisect_right_learn(arr, 20) # 2
    i = bisect_right_learn(arr, 25) # 2

    i = bisect_left_learn(arr, 5) # 0
    i = bisect_left_learn(arr, 10) # 0
    i = bisect_left_learn(arr, 15) # 1
    i = bisect_left_learn(arr, 20) # 1
    i = bisect_left_learn(arr, 25) # 2


    # this returns the index where it would inser the x value
    # nums = [2,3,4,4,4,7,9]
    #print(bisect_left_start(5, 3))  # 2
    nums = [1,4]
    print(binary_search_nearest_smallest(2))

    print(bisect_right(4)) #5
    print(bisect_left(4)) #2
    print(binary_search_nearest_largest(4)) #2
    print(binary_search_nearest_smallest(4)) #4
    print(search(4))

    print("not existing")
    print(bisect_right(5)) #5
    print(bisect_left(5)) #2
    print(binary_search_nearest_largest(5)) #5
    print(binary_search_nearest_smallest(5)) #4
    print(search(5))

    # if the element present in the array it will return itself
    print("next")
    print(bisect_right(7)) #2
    print(bisect_left(7)) #1
    print(binary_search_nearest_largest(7))#
    print(binary_search_nearest_smallest(7)) #5
    print(search(7))



    # this returns the nearest from the left

    # this returns the nearest from the right
