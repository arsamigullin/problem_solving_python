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


if __name__ == '__main__':

    # this returns the index where it would inser the x value
    # nums = [2,3,4,4,4,7,9]
    #print(bisect_left_start(5, 3))  # 2

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
