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
def threeSum(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    dic = {}
    for ele in nums:
        dic[ele] = dic.get(ele, 0) + 1

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


class Solution:
    def threeSum(self, nums):
        visited = set()
        res = []
        for i in range(len(nums) - 2):
            target = 0 - nums[i]
            d = {}
            for j in range(i + 1, len(nums)):

                if (min(nums[i], nums[j]), max(nums[i], nums[j])) in visited:
                    continue
                diff = target - nums[j]
                if diff in d:
                    visited.add((min(nums[i], nums[j]), max(nums[i], nums[j])))
                    res.append([nums[i], diff, nums[j]])
                d[nums[j]] = j
        return res

# O(n**2)
class SolutionPointers:
    def threeSum(self, nums):
        nums.sort()
        res = set()
        for i in range(len(nums)):
            target = 0 - nums[i]
            l = i + 1
            r = len(nums) - 1
            while l<r:
                lrsum = nums[l] + nums[r]
                if lrsum == target:
                    res.add((nums[i], nums[l], nums[r]))
                    r-=1
                    l+=1
                elif lrsum > target:
                    r-=1
                else:
                    l+=1
        return res


class SolutionPointersDic:
    def threeSum(self, nums):
        nums.sort()
        dic = {}
        for ele in nums:
            dic[ele] = dic.get(ele, 0) + 1
        res = set()
        keys = list(dic.keys())
        for i, k in enumerate(keys):
            if dic[k] >= 2 and len(nums)>2:
                target = 0 - k * 2
                if target in dic:
                    if target == k:
                        if dic[k]>=3:
                            res.add((k, k, target))
                    else:
                        res.add((k, k, target))
            target = 0 - k
            l = i + 1
            r = len(keys) - 1
            while l < r:
                if dic[keys[l]] >= 2:
                    if target == keys[l] * 2:
                        res.add((keys[l], keys[l], k))
                if dic[keys[r]] >= 2:
                    if target == keys[r] * 2:
                        res.add((keys[r], keys[r], k))
                lrsum = keys[l] + keys[r]
                if lrsum == target:
                    res.add((keys[i], keys[l], keys[r]))
                    r-=1
                    l+=1
                elif lrsum > target:
                    r -= 1
                else:
                    l += 1

        return res




if __name__ == "__main__":
    s= SolutionPointersDic()
    s.threeSum([-4,-2,1,-5,-4,-4,4,-2,0,4,0,-2,3,1,-5,0])
    print(s.threeSum([0,0]))
    print(s.threeSum([-1, -1, 0, 1, 2, -1, -4]))
    #threeSum([0,1,-1])
    #s.threeSum([-1,0,1,2,-1,-4])
    #print(threeSum([-1, -1, 0, 1, 2, -1, -4]))