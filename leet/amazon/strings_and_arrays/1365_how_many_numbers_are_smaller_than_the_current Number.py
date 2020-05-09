from typing import List


class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        numidx = [(i, v) for i, v in enumerate(nums)]
        numidx.sort(key=lambda x: x[1])
        res = [0] * len(nums)
        for i in range(1, len(numidx)):
            pi, pv = numidx[i - 1]
            ci, cv = numidx[i]
            if pv == cv:
                res[ci] = res[pi]
            else:
                res[ci] = i
        return res


class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        # sort them then then create hash map reconstruct the array
        sorted_num = sorted(nums)
        dic = {}
        for i, e in enumerate(sorted_num):
            dic.setdefault(e,i)
        res = []
        for e in nums:
            res.append(dic[e])
        return res