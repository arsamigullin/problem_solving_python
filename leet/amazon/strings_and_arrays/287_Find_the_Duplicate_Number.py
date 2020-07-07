from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

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