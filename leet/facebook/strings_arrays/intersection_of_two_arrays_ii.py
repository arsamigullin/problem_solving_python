# https://leetcode.com/problems/intersection-of-two-arrays-ii/
class Solution:
    def intersect(self, nums1: list, nums2: list) -> list:
        d1, d2 = {}, {}
        for i in range(len(nums1)):
            d1[nums1[i]] = d1.get(nums1[i], 0) + 1
        for i in range(len(nums2)):
            d2[nums2[i]] = d2.get(nums2[i], 0) + 1

        res = []
        keys = d1.keys() if len(d1) < len(d2) else d2.keys()
        for k in keys:
            if k in d1 and k in d2:
                times = min(d1[k], d2[k])
                for _ in range(times):
                    res.append(k)
        return res