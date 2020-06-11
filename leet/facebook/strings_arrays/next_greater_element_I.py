# this is monotonous stack technique
class Solution:
    def nextGreaterElement(self, nums1: list, nums2: list) -> list:
        stack = []
        res = {}

        for num in nums2:
            while stack and stack[-1] < num:
                # store the values directly to the dictionary
                res[stack[-1]] = num
                stack.pop()

            stack.append(num)

        ans = []
        for num in nums1:
            ans.append(res.get(num, -1))

        return ans

class MySolution:
    def nextGreaterElement(self, nums1: list, nums2: list) -> list:
        d = {v:i for i,v in enumerate(nums2)}
        next_greater = [-1] * len(nums2)
        stack = []
        for i in range(len(nums2)):
            while len(stack) > 0 and nums2[stack[-1]] < nums2[i]:
                next_greater[stack.pop()] = i
            stack.append(i)
        res= []
        for n1 in nums1:
            index = next_greater[d[n1]]
            res.append(-1 if index == -1 else nums2[index])
        return res