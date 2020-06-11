# Monotonous stack technique
# since after the first loop in the stack we will have the indices of the elements
# which didn't find their next greater, then we can iterate the second time if
# those elements will find its next greater among the element that behind them
class MySolution:
    def nextGreaterElements(self, nums: list) -> list:
        stack = []
        next_greater = [-1] * len(nums)
        for i in range(len(nums)):
            while len(stack) > 0 and nums[stack[-1]] < nums[i]:
                next_greater[stack.pop()] = nums[i]
            stack.append(i)
        for i in range(len(nums)):
            while len(stack) > 0 and nums[stack[-1]] < nums[i]:
                next_greater[stack.pop()] = nums[i]
        return next_greater


if __name__ == "__main__":
    s = MySolution()
    s.nextGreaterElements([1,3,3,2,1])