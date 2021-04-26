from typing import List

# the idea here is to find the window of size = sum(all ones in the array)
# with a maximum sum of ones within that window
# then, the total swaps will be um(all ones in the array) - (maximum sum of ones within that window)

# this is long running solution (836 ms)
class Solution1:
    def minSwaps(self, data: List[int]) -> int:
        ones = sum(data)
        l = r = 0
        cnt_one = max_one = 0
        while r < len(data):
            cnt_one += data[r]
            r += 1
            # move left boudary
            if r - l > ones:
                cnt_one -= data[l]
                l += 1
            # we want to find maximum ones within the sliding window
            max_one = max(max_one, cnt_one)
        return ones - max_one



if __name__ == '__main__':
    s = Solution2()
    s.subarraySum([1,0,1,0,1],1)