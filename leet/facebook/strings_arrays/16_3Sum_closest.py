from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        diff = float('inf')
        for k in range(n):
            i, j = k+1, n-1
            while i<j:
                threesum = nums[k] + nums[i] + nums[j]
                if target - threesum == 0:
                    return threesum
                # this just determines the closest difference between target and threesum
                if abs(target - threesum) < abs(diff):
                    # but we want to store here real difference
                    # since we need to return the sum of the three numbers
                    diff = target - threesum

                if target > threesum:
                    i+=1
                else:
                    j-=1
        # to get this calculation correct
        return target - diff

if __name__ == '__main__':
    s = Solution()
    s.threeSumClosest([-1,2,1,-4], 1)