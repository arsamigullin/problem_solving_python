class MySolution:
    def findDisappearedNumbers(self, nums: list) -> list:
        if not nums:
            return []
        nums.sort()
        #print(nums)
        res = []
        def append(start, end):
            while start < end:
                res.append(start)
                start+=1
        if nums[0] - 1 > 0:
            append(1, nums[0])
        for i in range(len(nums) - 1):
            if nums[i + 1] - nums[i] >= 2:
                append(nums[i] + 1, nums[i + 1])
        if len(nums) - nums[-1] > 0:
            append(nums[-1] + 1, len(nums) + 1)
        return res


#We will be negating the numbers seen in the array and use the sign of each of the numbers for finding our missing numbers.
# We will be treating numbers in the array as indices and mark corresponding locations in the array as negative.
class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        # Iterate over each of the elements in the original array
        for i in range(len(nums)):

            # Treat the value as the new index
            new_index = abs(nums[i]) - 1

            # Check the magnitude of value at this new index
            # If the magnitude is positive, make it negative
            # thus indicating that the number nums[i] has
            # appeared or has been visited.
            if nums[new_index] > 0:
                nums[new_index] *= -1

        # Response array that would contain the missing numbers
        result = []

        # Iterate over the numbers from 1 to N and add all those
        # that have positive magnitude in the array
        for i in range(1, len(nums) + 1):
            if nums[i - 1] > 0:
                result.append(i)

        return result