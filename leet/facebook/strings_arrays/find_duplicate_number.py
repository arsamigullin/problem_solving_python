# this problem
#https://leetcode.com/problems/find-the-duplicate-number/

# one of the approach is similar to 
# find_all_duplicates_in_an_array.py - https://leetcode.com/problems/find-all-duplicates-in-an-array/

# very similar problem
# https://leetcode.com/problems/linked-list-cycle-ii/

import typing
List = typing.List
class Solution:
    def findDuplicate_approach1(self, nums: List[int]) -> int:
        '''
        Cycle detection
        since the values of the array will essntially be within the index range (0..n)
        we can mark the visited element and once we visit it again we found the duplicate
        '''
        for v in nums:
            index = abs(v) - 1
            if nums[index] > 0:
                nums[index]*=-1
            else:
                return nums[index]
        return None

    def findDuplicate_approach2(self, nums: List[int]) -> int:
        '''
        this approach uses Tortoise and Hare cycle detection algorithm
        https://leetcode.com/problems/linked-list-cycle-ii/

        tortoise is represented as nums[i]
        hare is represented as nums[nums[i]], so here we do two steps
        '''
        tortoise = hare = nums[0]
        while True:
            '''
            here we are detecting cycle
            '''
            tortoise = nums[tortoise]
            hare = nums[nums[hare]]
            if tortoise == hare:
                break

        # now let's define entrance of cycle
        # this is the general algorithe for finding entrance to cycle 
        # just remember it
        # it also is used https://leetcode.com/problems/linked-list-cycle-ii/
        ptr1 = nums[0]
        ptr2 = tortoise
        while ptr1!=ptr2:
            '''
            since the cycle can be detected at any point (not necessary at the duplicate point like with [3,1,3,4,2])
            we need to define entrance point of cycle
            '''
            ptr1 = nums[ptr1]
            ptr2 = nums[ptr2]

        return ptr1

if __name__ == "__main__":
    s = Solution()
    print(s.findDuplicate_approach2([2,5,9,6,9,3,8,9,7,1]))
        

        
