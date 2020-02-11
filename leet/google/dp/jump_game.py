# https://leetcode.com/problems/jump-game/
# U - unknown (we didn't visited it yet)
# G - good (We call a position in the array a "good index" if starting at that position, we can reach the last index.)
# B - bad (that index is called a "bad index". The problem then reduces to whether or not index 0 is a "good index".)

#Algo
# just a reminder. At each position we have a number we can jump from current position
# let say we have [1,2,3,4] array. At index 0 we can jump at most to 0+2 index
#Algo
# 1. init memo array with the same length as nums and fill it with U
# 2. Starting from 0 index identify the max index you can jump to
# and iterate over this distance starting from position + 1
# 3. if the last index is reachable from the current index this current is going to be good

#This is the inefficient solution where we try every single jump pattern that takes us from
# the first position to the last. We start from the first position and jump to every index that
# is reachable. We repeat the process until last index is reached. When stuck, backtrack.

#TLE
# Top-down approach
class Solution:
    def canJump(self, nums: list) -> bool:
        memo = ['U'] * len(nums)
        memo[-1] = 'G'
        def canjmp(cur_index, nums):
            if memo[cur_index]!='U':
                return  memo[cur_index] == 'G'
            max_distance_to_jump_from_cur_index = cur_index + nums[cur_index]
            for i in range(cur_index + 1, max_distance_to_jump_from_cur_index + 1):
                if canjmp(i, nums):
                    memo[i] = 'G'
                    return True
            memo[i] = 'B'
            return False
        return canjmp(0, nums)

if __name__ == "__main__":
    s = Solution()
    s.canJump([2,3,1,1,4])

# In bottom-up approach we start from the end of array
# TLE
class Solution:
    def canJump(self, nums):
        memo = ['U'] * len(nums)
        memo[-1] = 'G'
        for i in range(len(nums) - 2, -1 , -1):
            max_distance_to_jump = i + nums[i]
            for j in range(i+1, max_distance_to_jump + 1):
                if memo[j] == 'G':
                    memo[i] = 'G'
                    break
        return memo[0] == 'G'

# Accepted
# Greedy
# let's consider an example [2,3,1,1,4]
# we start from the last index and move back to the first index
# the last position is gonna be the last index
# if the current index plus its value is greater than last pos assign las position the current index
# i+nums[i] >= lastpos means we can reach lastpos
class Solution:
    def canJump(self, nums: list) -> bool:
        lastpos = len(nums) - 1
        for i in range (len(nums) - 1, -1, -1):
            if i+nums[i] >= lastpos:
                lastpos = i
        return lastpos == 0


class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        queue = collections.deque((root, 0))
        l = -1
        n = Node()

        def find(queue, prev, l):
            if queue:
                node, level = queue.popleft()
                if l == level:
                    prev.next = node
                else:
                    prev.next = None
                if node.left is not None:
                    queue.append((node.left, level + 1))
                if node.right is not None:
                    queue.append((node.right, level + 1))
                find(queue, node, level)
        find(queue, n, -1)
        return n.next

