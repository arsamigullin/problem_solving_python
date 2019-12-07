def threeSum(nums):
    d = {v: i for i, v in enumerate(nums)}
    n = len(nums)
    s = set()
    for i in range(0, n):
        for j in range(i + 1, n):
            two = nums[i] + nums[j]
            third = 0 - two
            if third in d:
                if d[third]>j:
                    lo = min(nums[i],nums[j], third);
                    hi = max(nums[i],nums[j], third);
                    s.add((lo, 0 - hi - lo, hi))
    return s

if __name__ == "__main__":
    threeSum([0,1,-1])
    threeSum([-1, 0, 1, 2, -1, -4])