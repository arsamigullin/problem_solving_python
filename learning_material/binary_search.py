import bisect


#nums = [1,2,3,4]
# NOTE: bisect right and bisect left are different only in the >=
#     The return value i is such that all e in a[:i] have e <= x, and all e in
#     a[i:] have e > x.

# three cases
# 1. x is in array, it will return its index
# 2. x is in array but there are multiple x in the array. It will return index of the left most x
# 3. x is not in an array, it will return index of the index of the first greater value
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
# three cases
# 1. x is in array, it will return its index
# 2. x is in array but there are multiple x in the array. It will return index of the left most x
# 3. x is not in an array, it will return index of the index of the first greater value
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


if __name__ == '__main__':
    nums = [2,3,4,4,4,7,9]
    print(bisect_left(3))
    print(bisect_left(4))
    print(bisect_left(5))
    print(bisect.bisect_left(nums, 3))
    print(bisect.bisect_left(nums, 4))
    print(bisect.bisect_left(nums, 5))
    print('hello')
    print(bisect_right(3))
    print(bisect_right(4))
    print(bisect_right(5))
    print(bisect.bisect_right(nums, 3))
    print(bisect.bisect_right(nums, 4))
    print(bisect.bisect_right(nums, 5))

