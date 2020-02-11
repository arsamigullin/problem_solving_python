
# we maintain three pointers here
# curr_min is to take care of negative numbers
# to take into account the product with two negative numbers

class Solution:
    def maxProduct(self, nums: list) -> int:
        curr_max = nums[0]
        curr_min = nums[0]
        global_max = nums[0]

        for i in range(1, len(nums)):
            prev_max = curr_max # since prev_max is used to calculate curr_min we store it here
            # get current max
            curr_max = max(curr_max * nums[i], curr_min * nums[i], nums[i])
            # get current min
            # note: it is almost the same as in max argument
            curr_min = min(prev_max * nums[i], curr_min * nums[i], nums[i])
            global_max = max(global_max, curr_max)
        return global_max



class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_dp = [0]*len(nums)
        min_dp = [0]*len(nums)
        max_dp[0], min_dp[0] = nums[0], nums[0]
        for i in range(1, len(nums)):
            max_dp[i] = max(max_dp[i-1]*nums[i], min_dp[i-1]*nums[i], nums[i])
            min_dp[i] = min(max_dp[i-1]*nums[i], min_dp[i-1]*nums[i], nums[i])
        return max(max_dp)


class Solution:
    # @param A, a list of integers
    # @return an integer
    def maxProduct(self, A):
        minNow = A[0]
        maxNow = A[0]
        output = maxNow
        for num in A[1:]:
        	minPrev = minNow
        	maxPrev = maxNow
        	minNow = min(num, minPrev * num, maxPrev * num)
        	maxNow = max(num, minPrev * num, maxPrev * num)
        	output = max(output, maxNow)
        return output

if __name__ == "__main__":
    s = Solution()
    s.maxProduct([1, 3, -3, -12])