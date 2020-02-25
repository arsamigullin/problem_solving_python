#https://leetcode.com/problems/path-sum-iv/
# since we know in advance that level will not be exceeded 4 and position will not be exceeded 8
# i.e. this is max tree we will have
#       1
#      / \
#     2   3
#    /\   /\
#   4  5  6  7
#  / \ /\ /\ /\
# 8  9 1 2 3 4 5
# we can convert the tree to the dict(list)
# where key is level, index of list is position and value at that incex is value

class Solution:
    def pathSum(self, nums: List[int]) -> int:
        if not nums:
            return 0
        # we create that dict before
        d = {0:[None]*1, 1:[None]*2, 2:[None]*4, 3:[None]*8}
        
        # collect nodes to the dict
        for num in nums:
            level = num//100
            position = (num - level * 100)//10
            val = num - level * 100 - position * 10
            d[level - 1][position-1] = val
        total = 0

        def find(level, pos, res):
            nonlocal total
            if d[level][pos] is not None:
                # define positions and level for left and right nodes
                lpos = pos * 2 
                rpos = pos * 2 + 1
                nxt_lvl = level + 1
                # if cur level is 3 (which is max since we start level from 0) or both of children are None 
                # then we increase the total
                if level >=3 or (d[nxt_lvl][lpos] is None and d[nxt_lvl][rpos] is None):
                    total+=res + d[level][pos]
                    return
                # continue the same for left and right node
                find(nxt_lvl, lpos, res + d[level][pos])
                find(nxt_lvl, rpos, res + d[level][pos])
        find(0, 0, 0)
        return total

                