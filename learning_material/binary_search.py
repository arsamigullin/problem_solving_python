import bisect

nums = [2,3,5,5,5,7,9]

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
        if x > nums[mid]:
            lo = mid+1
        else:
            hi = mid
    return lo

#
def binary_search_nearest_from_the_left(guess):
    if guess > nums[-1]:
        return len(nums) - 1
    lo = 0
    hi = len(nums) - 1
    res = -1
    while lo <= hi:
        mid = (lo + hi) // 2
        if guess >= nums[mid]:
            lo = mid + 1
            res = mid
        else:
            hi = mid - 1
    return res

def binary_search_nearest_from_the_left(guess):
    if guess > nums[-1]:
        return len(nums) - 1
    lo = 0
    hi = len(nums) - 1
    res = -1
    while lo <= hi:
        mid = (lo + hi) // 2
        if guess >= nums[mid]:
            lo = mid + 1
            res = mid
        else:
            hi = mid - 1
    return res

def binary_search_nearest_from_the_right(guess):
    if guess > nums[-1]:
        return len(nums) - 1
    lo = 0
    hi = len(nums) - 1
    res = -1
    while lo <= hi:
        mid = (lo + hi) // 2
        if guess >= nums[mid]:
            lo = mid + 1
        else:
            res = mid
            hi = mid - 1
    return res

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
    # nums = [2,3,5,5,5,7,9]
    # this returns the index where it would inser the x value
    print(bisect_right(5)) #5
    print(bisect_left(5)) #2
    print(binary_search_nearest_from_the_left(5)) #4
    print(binary_search_nearest_from_the_right(5)) #5
    print(search(5))

    print("not existing")
    print(bisect_right(4)) #5
    print(bisect_left(4)) #2
    print(binary_search_nearest_from_the_left(4)) #4
    print(binary_search_nearest_from_the_right(4)) #5
    print(search(4))
    # if the element present in the array it will return itself
    print("next")
    print(bisect_right(3)) #2
    print(bisect_left(3)) #1
    print(binary_search_nearest_from_the_left(3))#
    print(binary_search_nearest_from_the_right(3)) #5
    print(search(3))



    # this returns the nearest from the left

    # this returns the nearest from the right
