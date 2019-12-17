# this runs around 1010ms
def threeSum(nums):
    #d = dict()
    #for i in range(len(nums)):
        #d[i] = nums
    d = {v: i for i, v in enumerate(nums)}
    n = len(nums)
    s = set()
    i=0
    inc_i = 1
    is_initial = True
    while i < n:
        for j in range(i + 1, n):
            if nums[i] == nums[j]:
                if is_initial:
                    inc_i += 1
            else:
                is_initial = False
            two = nums[i] + nums[j]
            third = 0 - two
            if third in d:
                if d[third]>j:
                    lo = min(nums[i],nums[j], third);
                    hi = max(nums[i],nums[j], third);
                    s.add((lo, 0 - hi - lo, hi))
        i+= inc_i
        inc_i = 1
        is_initial = True
    return s

# this runs much faster (300ms)
def threeSum(self, nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    dic = {}
    for ele in nums:
        if ele not in dic:
            dic[ele] = 0
        dic[ele] += 1

    if 0 in dic and dic[0] > 2:
        rst = [[0, 0, 0]]
    else:
        rst = []

    pos = [p for p in dic if p > 0]
    neg = [n for n in dic if n < 0]

    for p in pos:
        for n in neg:
            inverse = -(p + n)
            if inverse in dic:
                if inverse == p and dic[p] > 1:
                    rst.append([n, p, p])
                elif inverse == n and dic[n] > 1:
                    rst.append([n, n, p])
                elif inverse < n or inverse > p or inverse == 0:
                    rst.append([n, inverse, p])

    return rst


if __name__ == "__main__":
    #threeSum([0,1,-1])
    print(threeSum([-1, -1, 0, 1, 2, -1, -4]))