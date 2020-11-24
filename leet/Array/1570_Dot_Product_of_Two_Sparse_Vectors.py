# My solution
class SparseVector:
    def __init__(self, nums: List[int]):
        self.nums = nums
        self.nonzero = []
        for i, n in enumerate(nums):
            if n!=0:
                self.nonzero.append(i)

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        res = 0
        for i in self.nonzero:
            res += self.nums[i]*vec.nums[i]
        return res

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)


  class SparseVector:
    def __init__(self, nums: List[int]):
        self.index2val = {i:nums[i] for i in range(len(nums)) if nums[i]}
    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        ans = 0
        #case1: other vector is a sparse vector
        if len(self.index2val) > len(vec.index2val):
            for i in vec.index2val:
                if i in self.index2val:
                    ans += vlec.index2val[i] * self.index2va[i]
        #case2: this vector is a sparse vector
        else:
            for i in self.index2val:
                if i in vec.index2val:
                    ans += vec.index2val[i] * self.index2val[i]
        return ans