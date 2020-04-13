import typing
List = typing.List
# this problem
# https://leetcode.com/problems/maximum-distance-in-arrays/

class Solution:
    '''
    let's consider example
    [[1,4]
     [0,5]
     [-2,6]]

     min_val = 1, max_val = 4
     each iteration will calculate the distance based on previous found min_val and max_val
     and current min_val and max_val

     even if cur_min and cur_max are from the same row(according to problem each array  picks only one)
     inside of loop we calculate the distance using min_val and max of i row (cur_max)
     and using min val of i row (cur_min) and max_val

     so, the distance is never calculated on the same row of min and max
     I iteration

    '''
    def maxDistance(self, arrays: List[List[int]]) -> int:
        res = 0 # this keeps actual distance
        min_val = arrays[0][0]
        max_val = arrays[0][-1]
        for i in range(1, len(arrays)):
            cur_min = arrays[i][0]
            cur_max = arrays[i][-1]
            res = max(res, max(abs(cur_max - min_val), abs(max_val - cur_min)))
            min_val = min(min_val, cur_min)
            max_val = max(max_val, cur_max)
        return res


if __name__ == "__main__":
    s = Solution()
    s.maxDistance([[1],[2]])