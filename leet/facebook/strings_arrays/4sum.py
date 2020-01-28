class Solution:
# @return a list of lists of length 4, [[val1,val2,val3,val4]]
     def fourSum(self, nums: list, target: int) -> list:
            nums.sort()

            n,res=len(nums),set()
            for i in range(n-3):
                for j in range(i+1,n-2):
                    l,r=j+1,n-1
                    while l<r:
                        sum=nums[i]+nums[j]+nums[l]+nums[r]
                        if sum > target: r-=1
                        elif sum<target: l+=1
                        else:
                            a=(nums[i],nums[j],nums[l],nums[r])
                            res.add(a)
                            l+=1;r-=1
            return list(res)


class Solution:
    # def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
    #   nums = sorted(nums)
    #   return self.kSum(nums, 0, 4, target)
    # def kSum(self, nums: List[int], start: int, k: int, target: int) -> List[List[int]]:
    #   ln = len(nums)
    #   res =[]
    #   if k == 2:
    #     left = start; right = ln - 1
    #     while left < right:
    #       ab = nums[left] + nums[right];
    #       #find a pair
    #       if ab == target:
    #         temp = []
    #         temp.append(nums[left])
    #         temp.append(nums[right])
    #         res.append(temp)
    #         #skip duplication
    #         while left<right and nums[left] == nums[left+1]:
    #           left+=1
    #         while left<right and nums[right-1] == nums[right]:
    #           right-=1
    #         left+=1; right-=1
    #         #move left bound
    #       elif ab < target:
    #         left+=1
    #         #move right bound
    #       else:
    #         right-=1
    #   else:
    #     for i in range(start, ln - k + 1):
    #       if i > start and nums[i] == nums[i - 1]: continue
    #       #use current number to reduce ksum into k-1sum
    #       temp = self.kSum(nums, i + 1, k - 1, target - nums[i])
    #       if temp is not None:
    #         #add previous results
    #         for t in temp:
    #           t.insert(0, nums[i])
    #         res.extend(temp)
    #   return res
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        if not nums:
            return []
        nums.sort()

        # length
        L = len(nums)
        N = {j: i for i, j in enumerate(nums)}
        # final set
        S = set()
        # largest element
        M = nums[-1]
        for i in range(L - 3):
            a = nums[i]
            if a + 3 * M < target: continue
            if 4 * a > target: break
            for j in range(i + 1, L - 2):
                b = nums[j]
                if a + b + 2 * M < target: continue
                if a + 3 * b > target: break
                for k in range(j + 1, L - 1):
                    c = nums[k]
                    d = target - (a + b + c)
                    if d < c: break
                    if d > M: continue
                    if d in N and N[d] > k: S.add((a, b, c, d))

        return S